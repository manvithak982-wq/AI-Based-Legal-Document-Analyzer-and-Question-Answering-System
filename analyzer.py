import re
from config import CLAUSE_TYPES


class LegalAnalyzer:

    def __init__(self):

        self.clause_keywords = {

            "Payment": [
                "payment",
                "payments",
                "pay",
                "fee",
                "fees",
                "invoice",
                "amount",
                "compensation",
                "pricing",
                "price",
                "billing"
            ],

            "Termination": [
                "termination",
                "terminate",
                "terminated",
                "cancel",
                "expiration",
                "expiry",
                "notice",
                "notice period"
            ],

            "Confidentiality": [
                "confidential",
                "confidentiality",
                "nda",
                "non disclosure",
                "non-disclosure",
                "secret"
            ],

            "Liability": [
                "liability",
                "liable",
                "damages",
                "loss",
                "responsible"
            ],

            "Force Majeure": [
                "force majeure",
                "act of god",
                "pandemic",
                "war",
                "earthquake",
                "flood"
            ],

            "Governing Law": [
                "governing law",
                "jurisdiction",
                "court",
                "laws of"
            ],

            "Intellectual Property": [
                "copyright",
                "patent",
                "trademark",
                "intellectual property",
                "ownership"
            ],

            "Warranty": [
                "warranty",
                "guarantee",
                "warrant"
            ],

            "Obligations": [
                "shall",
                "must",
                "required",
                "obligation",
                "agree to"
            ],

            "Rights": [
                "right",
                "rights",
                "permission",
                "authority"
            ],

            "Indemnity": [
                "indemnity",
                "indemnify"
            ],

            "Assignment": [
                "assignment",
                "assign"
            ],

            "Dispute Resolution": [
                "arbitration",
                "mediation",
                "dispute"
            ]
        }



    # ==========================================
    # CLAUSE DETECTION
    # ==========================================

    def detect_clauses(self, text, page_number):

        clauses = []

        text_lower = text.lower()


        for clause_name, keywords in self.clause_keywords.items():

            matched = []


            for keyword in keywords:

                if keyword in text_lower:
                    matched.append(keyword)


            if matched:

                clauses.append({

                    "type": clause_name,

                    "text": text[:500],

                    "page": page_number

                })


        return clauses



    # ==========================================
    # RISK DETECTION
    # ==========================================

    def detect_risks(self, text, page_number):

        risks = []


        risk_keywords = {

            "High": [
                "penalty",
                "lawsuit",
                "breach",
                "default",
                "legal action"
            ],


            "Medium": [
                "late payment",
                "dispute",
                "liability",
                "indemnity",
                "confidential"
            ],


            "Low": [
                "notice",
                "permission",
                "approval"
            ]

        }


        text_lower = text.lower()



        for severity, keywords in risk_keywords.items():

            found = []


            for keyword in keywords:

                if keyword in text_lower:
                    found.append(keyword)



            if found:

                risks.append({

                    "severity": severity,

                    "reason":
                    "Risk detected due to: "
                    + ", ".join(found),

                    "page": page_number

                })


        return risks



    # ==========================================
    # REMOVE DUPLICATES
    # ==========================================

    def remove_duplicates(self, items):

        result = []

        seen = set()


        for item in items:

            key = str(item)


            if key not in seen:

                seen.add(key)

                result.append(item)


        return result



    # ==========================================
    # SUMMARY
    # ==========================================

    def create_summary(self, pdf_data, clauses, risks):

        pages = len(pdf_data["pages"])


        summary = f"""
Legal Document Analysis Summary

Total Pages:
{pages}

Clauses Detected:
{len(clauses)}

Risks Detected:
{len(risks)}

The document was analyzed for legal clauses,
obligations, risks and important information.
"""


        return summary.strip()



    # ==========================================
    # MAIN ANALYZER
    # ==========================================

    def analyze(self, pdf_data):

        clauses = []

        risks = []


        print("\n========== ANALYZING DOCUMENT ==========")



        for page in pdf_data["pages"]:


            page_number = page["page"]

            text = page["text"]



            page_clauses = self.detect_clauses(
                text,
                page_number
            )


            page_risks = self.detect_risks(
                text,
                page_number
            )



            clauses.extend(page_clauses)

            risks.extend(page_risks)



        clauses = self.remove_duplicates(clauses)

        risks = self.remove_duplicates(risks)



        print("Clauses:", len(clauses))

        print("Risks:", len(risks))



        return {

            "clauses": clauses,

            "risks": risks,

            "summary": self.create_summary(
                pdf_data,
                clauses,
                risks
            )

        }



# ==========================================
# OBJECT
# ==========================================

analyzer = LegalAnalyzer()



if __name__ == "__main__":

    print("Legal Analyzer Ready")