import fitz
import re

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class PDFProcessor:

    def __init__(self):
        pass

    # =====================================================
    # CLEAN TEXT
    # =====================================================

    def clean_text(self, text):

        if not text:
            return ""

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove repeated dots
        text = re.sub(r"\.{2,}", ".", text)

        # Remove new lines and tabs
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")

        return text.strip()

    # =====================================================
    # EXTRACT PDF
    # =====================================================

    def extract_text(self, filepath):

        document = fitz.open(filepath)

        pages = []

        for page_number in range(len(document)):

            page = document.load_page(page_number)

            text = page.get_text("text")

            cleaned = self.clean_text(text)

            pages.append({
                "page": page_number + 1,
                "text": cleaned
            })

        document.close()

        return pages

    # =====================================================
    # CHUNK SINGLE PAGE
    # =====================================================

    def chunk_page(self, text, page_number):

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + CHUNK_SIZE

            chunk_words = words[start:end]

            chunk = " ".join(chunk_words)

            if chunk.strip():

                chunks.append({
                    "page": page_number,
                    "text": chunk,
                    "words": len(chunk_words)
                })

            if end >= len(words):
                break

            start = end - CHUNK_OVERLAP

            if start < 0:
                start = 0

        return chunks

    # =====================================================
    # CREATE CHUNKS
    # =====================================================

    def create_chunks(self, pages):

        all_chunks = []

        for page in pages:

            page_chunks = self.chunk_page(
                page["text"],
                page["page"]
            )

            all_chunks.extend(page_chunks)

        return all_chunks

    # =====================================================
    # DOCUMENT STATISTICS
    # =====================================================

    def statistics(self, pages, chunks):

        total_words = sum(
            len(page["text"].split())
            for page in pages
        )

        return {
            "pages": len(pages),
            "chunks": len(chunks),
            "words": total_words
        }

    # =====================================================
    # COMPLETE PROCESS
    # =====================================================

    def process(self, filepath):

        pages = self.extract_text(filepath)

        print("\n========== PDF TEXT ==========")
        print("Pages:", len(pages))

        for page in pages:
            print(f"\n----- Page {page['page']} -----")
            print(page["text"][:500])

        chunks = self.create_chunks(pages)

        print("\n========== CHUNKS ==========")
        print("Total Chunks:", len(chunks))

        for i, chunk in enumerate(chunks[:5]):
            print(f"\n----- Chunk {i+1} -----")
            print(chunk)

        stats = self.statistics(
            pages,
            chunks
        )

        return {
            "pages": pages,
            "chunks": chunks,
            "total_pages": stats["pages"],
            "total_chunks": stats["chunks"],
            "total_words": stats["words"]
        }


# =====================================================
# OBJECT
# =====================================================

processor = PDFProcessor()


def process_pdf(filepath):
    return processor.process(filepath)


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":
    print("PDF Processor Ready")