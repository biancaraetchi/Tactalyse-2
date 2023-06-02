from app.pdf_generator.generators.comparison_pdf import ComparisonPDF
from app.pdf_generator.generators.standard_pdf import StandardPDF


class PDFService:
    def create_pdf(self, param_map):
        """
        Function that retrieves a generated football analysis report for further use.

        :param param_map: Map containing all parameters needed to generate a PDF.
        :return: The PDF generated based on passed parameters and plots, in byte form.
        """
        if param_map.get('compare_name') is None:
            return self.create_standard_pdf(param_map)
        else:
            return self.create_comparison_pdf(param_map)


    def create_standard_pdf(self, param_map):
        generator = StandardPDF()
        return generator.generate_pdf(param_map)


    def create_comparison_pdf(self, param_map):
        generator = ComparisonPDF()
        return generator.generate_pdf(param_map)
