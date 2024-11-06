from abc import ABC, abstractmethod

#metaklasa do śledzenia rejestracji fabryk
class FactoryMeta(type):
    factories = {}

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if not name.startswith('Abstract'):
            FactoryMeta.factories[name] = new_cls
        return new_cls

#klasa abstrakcyjna dla dokumentów
class AbstractDocument(ABC):
    @abstractmethod
    def generate_content(self):
        pass

    def display(self):
        print("Displaying Content")
        print(self.generate_content())


#konkretna implementacja dokumentów
class InvoiceDocument(AbstractDocument):
    def generate_content(self):
        return "Treśc faktury: Detale trasakcji, kwoty, daty."
    
class ReportDocument(AbstractDocument):
    def generate_content(self):
        return "Treśc raportu: Analizy danych, podsumowanie miesięczne."
    
#klasa abstrakcyjna dla fabryk dokumentów
class AbstractDocumentFactory(ABC,metaclass=FactoryMeta):
    @abstractmethod
    def create_document(self) -> AbstractDocument:
        pass
    
#konkretne fabryki dokumentów
class InvoiceFactory(AbstractDocumentFactory):
    def create_document(self) -> AbstractDocument:
        return InvoiceDocument()
    
class ReportFactory(AbstractDocumentFactory):
    def create_document(self) -> AbstractDocument:
        return ReportDocument()
    
#funkcja kliencka
def client_code(factory:AbstractDocumentFactory):
    document = factory.create_document()
    document.display()
    
