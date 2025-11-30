from flask import Blueprint, request, jsonify, render_template, make_response
from weasyprint import HTML
import logging

export_bp = Blueprint('export', __name__, url_prefix='/api/export', template_folder='../templates')

@export_bp.route('/pdf', methods=['POST'])
def export_pdf():
    """
    Exports an itinerary as a PDF.
    """
    itinerary_data = request.get_json()

    try:
        html_string = render_template('itinerary.html', **itinerary_data)

        pdf = HTML(string=html_string).write_pdf()

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=itinerary.pdf'

        return response

    except Exception as e:
        logging.exception("Error generating PDF")
        return jsonify({"error": f"Failed to generate PDF: {str(e)}"}), 500
