const profiles = document.querySelector('.dog-profiles');
const profileCount = profiles.children.length;
let currentIndex = 0;

function moveProfiles() {
    profiles.style.transform = `translateX(-${currentIndex * 260}px)`;
    currentIndex = (currentIndex + 1) % profileCount;
}

setInterval(moveProfiles, 1000);

// script.js
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter');
  
  counters.forEach(counter => {
    counter.innerText = '0';
    
    const updateCounter = () => {
      const target = +counter.getAttribute('data-target');
      const current = +counter.innerText;
      
      const increment = target / 200;
      
      if (current < target) {
        counter.innerText = `${Math.ceil(current + increment)}`;
        setTimeout(updateCounter, 10);
      } else {
        counter.innerText = target;
      }
    };
    
    updateCounter();
  });
});



