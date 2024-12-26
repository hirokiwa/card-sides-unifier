import fitz  # PyMuPDF
import os

def merge_halves(pdf_front_path, pdf_back_path, pdf_out_path):
  # Open the two input PDFs
  doc_front = fitz.open(pdf_front_path)
  doc_back = fitz.open(pdf_back_path)

  # Create a new PDF
  doc_out = fitz.open()

  # Determine how many pages to process (assuming both have the same number of pages)
  page_count = min(len(doc_front), len(doc_back))

  for i in range(page_count):
    # Load the pages
    page_front = doc_front[i]
    page_back = doc_back[i]

    # Get their rectangles (page dimensions)
    rect_front = page_front.rect
    rect_back = page_back.rect

    # You can adjust this percentage as needed
    x_break_point_percent = 45

    # Calculate crop widths for front & back
    front_half_rect_x = (rect_front.x0 + rect_front.x1) / 100 * x_break_point_percent
    back_half_rect_x  = (rect_back.x0 + rect_back.x1) / 100 * (100 - x_break_point_percent)

    # Crop to the front half of front.pdf
    front_half_rect = fitz.Rect(
      rect_front.x0,
      rect_front.y0,
      front_half_rect_x,
      rect_front.y1
    )

    # Crop to the back half of back.pdf
    back_half_rect = fitz.Rect(
      rect_back.x0,
      rect_back.y0,
      back_half_rect_x,
      rect_back.y1
    )

    # The new page width is the sum of the widths of the two halves
    new_page_width = front_half_rect.width + back_half_rect.width
    # Height is taken as the max of both page heights (usually they match)
    new_page_height = max(rect_front.height, rect_back.height)

    # Create a new page in the output PDF
    new_page = doc_out.new_page(width=new_page_width, height=new_page_height)

    # Destination rectangle for front half in the new page
    front_dest_rect = fitz.Rect(
      0,
      0,
      front_half_rect.width,
      new_page_height
    )

    # Destination rectangle for back half in the new page
    back_dest_rect = fitz.Rect(
      front_half_rect.width,
      0,
      front_half_rect.width + back_half_rect.width,
      new_page_height
    )

    # Place (show) the front half of the page
    new_page.show_pdf_page(
      front_dest_rect,
      doc_front,  # source document
      i,      # page index in source
      clip=front_half_rect
    )

    # Place (show) the back half of the page
    new_page.show_pdf_page(
      back_dest_rect,
      doc_back,   # source document
      i,      # page index in source
      clip=back_half_rect
    )

  # Save and close everything
  doc_out.save(pdf_out_path)
  doc_out.close()
  doc_front.close()
  doc_back.close()

if __name__ == "__main__":
  # Get the script's directory
  script_dir = os.path.dirname(os.path.abspath(__file__))

  # Define the input/output paths
  front_pdf_path = os.path.join(script_dir, "pdf", "front-side.pdf")
  back_pdf_path  = os.path.join(script_dir, "pdf", "back-side.pdf")
  merged_pdf_path = os.path.join(script_dir, "pdf", "both-sides.pdf")

  # Merge the PDFs
  merge_halves(front_pdf_path, back_pdf_path, merged_pdf_path)
  print(f"Merged PDF created: {merged_pdf_path}")
