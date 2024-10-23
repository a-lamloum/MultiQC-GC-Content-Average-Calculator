import sys
from bs4 import BeautifulSoup

def calculate_average_gc_content(html_file):
    try:
        # Read the HTML file
        with open(html_file, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Locate the specific table by its ID
        table = soup.find('table', id='general_stats_table_table')
        
        # Initialize variables to calculate the sum and count of GC content
        gc_sum = 0
        gc_count = 0

        # Iterate over each row in the table body
        for row in table.find('tbody').find_all('tr'):
            # Find the cell containing GC content
            gc_cell = row.find('td', class_='data-coloured fastqc-percent_gc')
            if gc_cell:
                # Extract the GC content percentage and convert it to float
                gc_value = float(gc_cell['data-sorting-val'])
                gc_sum += gc_value
                gc_count += 1

        # Calculate the average and round it to the nearest integer
        if gc_count > 0:
            average_gc = round(gc_sum / gc_count)
            print(f"The average GC content from {gc_count} samples is: {average_gc}")
        else:
            print("No GC content data found.")
    except FileNotFoundError:
        print(f"Error: The file '{html_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <html_file>")
        sys.exit(1)

    html_file = sys.argv[1]
    calculate_average_gc_content(html_file)
