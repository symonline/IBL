from flask import Flask, render_template, make_response
import pdfkit

def pdf_template():
    rendered = render_template('/app/templates/print.html')
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=right.pdf'

    return reponse
 