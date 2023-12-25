let search=document.querySelector('.main_input')
let a=document.querySelector('.minu')
let sa=0
let m=document.querySelector('.rasm_continer')
let inp=document.querySelector('input')
let minu_a=document.querySelector('.ps')
let sd=document.querySelector('a')
let ol=document.querySelectorAll('#pll')
let ss=document.querySelector('#ss')
window.onscroll= function(){
  if(window.pageYOffset>32) {
    a.classList.add('colo')
    sd.style.color='black'
    ol.forEach((e)=>{
      e.style.color='black'
    })
      }   
   else{
      a.classList.remove('colo')
      sd.style.color='white'
      ol.forEach((e)=>{
        e.style.color='white'
      })
  }
  
  if(window.pageYOffset>380){
    if(search){
    search.classList.add('search')
    }
  }
  else{
    if(search){
    search.classList.remove('search')}
  }
}
let img_soni=document.querySelectorAll('.rasm_continer img')
let j=1
setInterval(()=>{
     if(img_soni.length==j){
      j=0
      }
      m.style.transform=`translateY(${-j*100}%)`
j++
},4000)
