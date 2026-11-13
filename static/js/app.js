document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');

    if (!sidebar || !sidebarToggle) return;

    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');

        const isCollapsed = sidebar.classList.contains('collapsed');

        sidebarToggle.setAttribute('aria-expanded', String(!isCollapsed));
        sidebarToggle.setAttribute(
            'aria-label',
            isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'
        );
    });
});
