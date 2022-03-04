let profile_picture = document.getElementById('profile-picture')
let profile_dropdown = document.getElementById('profile-dropdown')

profile_picture.addEventListener("mouseenter", ()=>{
    profile_dropdown.style.display = 'block';
})

profile_dropdown.addEventListener('mouseleave', ()=>{
    profile_dropdown.style.display = 'none';
})

console.log('Connected');