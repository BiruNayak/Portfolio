import { servicesData } from '../data/services.js';
import { portfolioData } from '../data/portfolio.js';
 
export function generateServices() {
  const container = document.querySelector('.services-list');
  container.innerHTML = '';
  servicesData.forEach(service => {
    const div = document.createElement('div');
    div.innerHTML = `
      <i class="fa-solid ${service.icon}"></i>
      <h2>${service.title}</h2>
      <p>${service.description}</p>
      <a href="#">Learn More</a>
    `;
    container.appendChild(div);
  });
}

export function generatePortfolio() {
  const container = document.querySelector('.work-list');
  container.innerHTML = '';
  portfolioData.forEach(project => {
    const div = document.createElement('div');
    div.classList.add('work');
    div.innerHTML = `
      <img src="${project.image}">
      <div class="layer">
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <a href="#"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>
      </div>
    `;
    container.appendChild(div);
  });
}