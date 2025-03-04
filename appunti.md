# coordinates/indexes

if pixels_num == 25:
you can call in these ways:
1.  one dimensional index (0..24)
2.  by coordinates (col, row)

the first pixel in (1) way is `0` and `(0,0)` in the (2) way

the fourth pixel in (1) is `3` and `(3,0)` in the (2) way

the eighth pixel in (1) is `7` and `(1,1)` in the (2) way

12 = (2,2) => 2 + 2 * 5 = 12

3 = (3,0) => 3 + 0 * 5 = 3

18 = (3,3) => 3 + 3 * 5 = 18

you can convert from coordinates (2) to index in this way:
col + row * n_col = col + row * 5

```py
def xy2index(col, row, n_col):
    return col + row * n_col
```

conversion index to coordinates:

18 // 5 = 3 (row) 18 % 5 = 3 (col)

3 // 5 = 0 (row) 3 % 5 = 3 (col)

```py
def index2xy(index, n_rows, n_cols):
    return index // n_rows, index // n_cols
```

# colors

a color can be represented as a rgb triple (R, G, B) within 0-255 range. Alternately you can express a color as a hexadecimal number like `0xff0000` (red)

```py
def colortuple2colorint(rgbtuple):
    return (rgbtuple[0] << 16) + (rgbtuple[1] << 8) + rgbtuple[2]
```