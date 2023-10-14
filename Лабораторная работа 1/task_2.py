# TODO Найдите количество книг, которое можно разместить на дискете

size_of_floppy_disk = 1.44
count_pages_of_book = 100
count_rows_of_page = 50
count_symbols_of_row = 25
size_symbol = 4

size_in_bytes_of_floppy_disk = 1.44 * 1024 * 1024
count_books = size_in_bytes_of_floppy_disk // (count_pages_of_book * count_rows_of_page * count_symbols_of_row
                                               * size_symbol)
print("Количество книг, помещающихся на дискету:", int(count_books))
