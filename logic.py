from browser import document as D, html as H
D <= H.H1("Számok 0-tól 99-ig")
D <= H.TABLE(
    H.TR(
        H.TD(10*(i-1)+j-1, Class="x" if i == 1 or j == 1 else "x2") for j in range(1,11)
    ) for i in range(1,11)
)
