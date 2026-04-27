from pyscript import document

photos = [
    {"src": "img1.jpg", "caption": "CAT Activity"},
    {"src": "img2.jpg", "caption": "Christmas Party"},
    {"src": "img3.jpg", "caption": "Intramurals"},
]

gallery = document.getElementById("photo-gallery")

gallery = document.getElementById("photo-gallery")

gallery.style.display = "flex"
gallery.style.flexDirection = "column"
gallery.style.gap = "24px"
gallery.style.alignItems = "center"

for photo in photos:
    card = document.createElement("div")
    card.className = "photo-card"

    img = document.createElement("img")
    img.src = photo["src"]
    img.alt = photo["caption"]
    img.style.width = "400px"
    img.style.height = "250px"
    img.style.objectFit = "cover"
    img.style.borderRadius = "8px"

    caption = document.createElement("p")
    caption.className = "photo-caption"
    caption.textContent = photo["caption"]

    card.appendChild(img)
    card.appendChild(caption)
    gallery.appendChild(card)
