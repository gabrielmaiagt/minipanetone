// Configure os links reais de checkout para ativar as compras.
const checkoutLinks = { basico: 'https://pay.cakto.com.br/sx8qygn', completo: 'https://pay.cakto.com.br/63bx672' };
const plans = {
  basico: { name: 'Pacote Básico', price: 'R$ 12,90', description: 'Acesso à área completa: 80 receitas, PDFs, 11 aulas públicas de apoio e os 5 bônus.' },
  completo: { name: 'Pacote Completo', price: 'R$ 19,90', description: 'Acesso à área completa: 80 receitas, PDFs, 11 aulas públicas de apoio e os 5 bônus.' }
};
const dialog = document.querySelector('#checkout-dialog');
document.querySelectorAll('[data-plan]').forEach(button => {
  button.addEventListener('click', () => {
    const key = button.dataset.plan;
    const link = checkoutLinks[key];
    if (link) { window.location.assign(link); return; }
    const plan = plans[key];
    document.querySelector('#dialog-title').textContent = plan.name;
    document.querySelector('#dialog-description').textContent = plan.description;
    document.querySelector('#dialog-price').textContent = plan.price;
    dialog.showModal();
  });
});
document.querySelectorAll('.dialog-close, .dialog-return').forEach(button => button.addEventListener('click', () => dialog.close()));
dialog.addEventListener('click', event => {
  const bounds = dialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
});
