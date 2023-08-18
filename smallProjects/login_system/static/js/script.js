let xbut=document.getElementById('xbutt')
let pass= document.getElementById('pas')
let unlockButt=document.getElementById('lock')
let lockButt=document.getElementById('unlock')
function clicker() {
    xbut.classList.toggle('hidden')
}
function unlocker() {
    unlockButt.style.display="none"
    lockButt.style.display="flex"
    pass.type=("text")
}
function locker() {
    unlockButt.style.display="flex"
    lockButt.style.display="none"
    pass.type=("password")
}
