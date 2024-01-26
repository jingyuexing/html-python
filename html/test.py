
from htmlElement import createElement

if __name__ == '__main__':
    div = createElement("div")
    h1 = createElement("h1")
    h4 = createElement("h4")
    
    h1.appendChild(h4)
    h4.appendChild(div)
    
    div.classList.add(["a","b","c","d","e","f","g","h","i","j","k","l","m","n"])
    h1.setAttributes("dataset-name",12)
    h1.textContent = "this is h1 text"
    h1.style.display = "flex"
    h1.style.border = "1px solid #eee"
    
    h4.textContent = "this is text 4 node"
    h4.className = "flex justify-center"
    h1.className = "flex justify-center items-center nanoid"
    
    
    print(h1)