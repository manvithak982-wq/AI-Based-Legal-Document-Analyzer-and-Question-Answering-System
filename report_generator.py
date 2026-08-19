# =====================================================
# AI LEGAL DOCUMENT REPORT GENERATOR
# =====================================================


from datetime import datetime



def report_generator(document_text):

    """
    Generates a legal analysis report
    from extracted document text.
    """

    if not document_text:

        return {
            "summary": "No document content available.",
            "risk_level": "Unknown",
            "recommendations": []
        }



    text_length = len(document_text)



    summary = (
        "This document was analyzed using "
        "AI Legal Document Analyzer. "
        f"The document contains approximately "
        f"{text_length} characters."
    )



    risk_level = "Medium"



    recommendations = [

        "Review all legal clauses carefully.",

        "Verify obligations and responsibilities.",

        "Check dates, penalties and termination clauses.",

        "Consult a legal professional before final decisions."

    ]



    return {

        "summary": summary,

        "risk_level": risk_level,

        "recommendations": recommendations,

        "generated_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }