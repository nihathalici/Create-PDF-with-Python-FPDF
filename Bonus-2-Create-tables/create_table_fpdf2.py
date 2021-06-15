from fpdf import FPDF

class PDF(FPDF):
    def create_table(self, table_data, title='', data_size = 10, title_size = 12, align_data = 'L', align_header = 'L', cell_width = 'even', x_start = 'x_default', emphasize_data = [], emphasize_style = None, emphasize_color = (0,0,0)):

    """
    table_data:
                list of lists with first element being list of headers
    title:
                (Optional) title of table
    data_size:
                the font size if table data
    title_size:
                the font size of the title of the table 
    align_data:
                align table data  
                L = left align 
                C = center align 
                R = right align  
    align_header:
                align table header  
                L = left align 
                C = center align  
                R = right align  
    cell_width:
                even: evenly distribute cell/column width 
                uneven: base cell size on length of cell/column items 
                int: int value for width of each cell/column
                list of ints: list equal to number of columns with the width of each cell / column 
    x_start:
                where the left edge of table should start 
    emphasize_data:
                which data elements are to be emphasized - pass as list
                emphasize_style: the font style you want emphasized data to take 
                emphasize_color: emphasize color (if other than black)
    """
