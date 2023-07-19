//creamos un componente de menu
// componentes/c_menu.component.tsx
export default function C_menuComponent() {
    return (
        <>
            <h1>C Menu Component</h1>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/a_hola_mundo">A Hola mundo</a></li>
                <li><a href="/b_hola_mundo">B Hola mundo</a></li>
            </ul>
        </>
    )
}