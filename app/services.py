from aspose import words


class DOCX:

    @classmethod
    async def convert_in_pdf(cls, filename):
        docx = words.Document(filename)
        return docx.save(f'{filename}.pdf')