from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        self.print()

class PDFDocument(Document):
    
    def print(self):
        print("Друкую PDF документ")

class WordDocument(Document):
    
    def print(self):
        print("Друкую Word документ")

class ExcelDocument(Document):
    
    def print(self):
        print("Друкую Excel документ")

class DocumentFactory:

    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        elif doc_type == 'excel':
            return ExcelDocument()
        else:
            raise ValueError(f"Невідомий тип документу: {doc_type}")

if __name__ == "__main__":
    
    pdf_document = DocumentFactory.create_document('pdf')
    pdf_document.prepare_for_printing()
    
    print()

    word_document = DocumentFactory.create_document('word')
    word_document.prepare_for_printing()
    
    print()

    excel_document = DocumentFactory.create_document('excel')
    excel_document.prepare_for_printing()
