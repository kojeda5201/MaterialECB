export type PropiedadesComponente = {
    url: string;
    iteraciones: number;
    mostrar?:boolean;
}

export default function CComponente(
    props: PropiedadesComponente
){
    const {url, iteraciones, mostrar} = props
    const contenidoAdicional = ()=>{
        if(mostrar){
            return <p>Mostrar</p>
        }
        return <p>Ocultar</p>
    }
    return(
        <>
            <a href={url} target="_blank">IR A URL</a>
            <p>Iteracion: {iteraciones}</p>
            <p>Mostrar: {mostrar}</p>
            {contenidoAdicional()}
            {/*{mostrar ?<p>Mostrar con if contraido</p>:<p>Ocultar con if contraido</p>}*/}
        </>
    )
}