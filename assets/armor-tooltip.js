document.addEventListener("DOMContentLoaded", () => {
  let tooltip = document.querySelector(".mc-crafting-tooltip");
  if (!tooltip) {
    tooltip = document.createElement("div");
    tooltip.className = "mc-crafting-tooltip";
    tooltip.innerHTML = '<span class="mc-tooltip-title"></span><span class="mc-tooltip-subtitle"></span>';
    document.body.appendChild(tooltip);
  }

  // Use event delegation for dynamically added or reformatted elements
  document.body.addEventListener("mouseover", (e) => {
    const slot = e.target.closest('.mc-crafting-slot[data-tooltip-title]');
    if (!slot) return;
    
    tooltip.querySelector(".mc-tooltip-title").textContent = slot.getAttribute("data-tooltip-title");
    tooltip.querySelector(".mc-tooltip-subtitle").textContent = slot.getAttribute("data-tooltip-subtitle");
    tooltip.style.display = "block";
  });

  document.body.addEventListener("mousemove", (e) => {
    const slot = e.target.closest('.mc-crafting-slot[data-tooltip-title]');
    if (!slot) {
        tooltip.style.display = "none";
        return;
    }
    tooltip.style.left = (e.clientX + 12) + "px";
    tooltip.style.top = (e.clientY - 12) + "px";
  });

  document.body.addEventListener("mouseout", (e) => {
    const slot = e.target.closest('.mc-crafting-slot[data-tooltip-title]');
    if (!slot) return;
    
    // Check if the mouse actually left the slot (and didn't just enter a child like the img)
    if (!slot.contains(e.relatedTarget)) {
        tooltip.style.display = "none";
    }
  });
});
