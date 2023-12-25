let down=document.querySelector('#down')
let save_x=document.querySelector('.div_x')
let page=document.querySelector('.save_pag')
down.addEventListener('click', ()=>{
    page.classList.remove('save_none')
    page.preventDefault()
})
save_x.addEventListener('click', ()=>{
    page.classList.add('save_none')
})