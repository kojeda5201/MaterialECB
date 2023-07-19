'use client'
import {css} from '@emotion/react'
import styled from '@emotion/styled'
import cStyles from './c_estilos.module.css'


const pinkStyle = css`
  color: hotpink;
`
const TituloNaranja = styled.h1`
  color: orange;
  font-size: 8px;
`
const TituloVerde = styled.h1`
  color: green;
  font-size: 10px;
`
export default function DEstilosEjemplo() {
    const misEstilos ={
        color: '#fff',
        backgroundColor: 'back',
        borderBottom: '5px solid yellow'
    }
    return (
        <>
            {/*<p className={*/}
            {/*    style*/}
            {/*}>Hola pink</p>*/}
            <TituloNaranja>Titulo 1</TituloNaranja>
            <TituloVerde>Titulo 2</TituloVerde>
            <div className={pinkStyle as unknown as string}>
                Texto pink
            </div>
            <p className={cStyles.rojo}>Clase rojo</p>
            <p style={misEstilos}>Mis estilos</p>
            <p style={
                {
                    color: 'back',
                    backgroundColor: '#fff',
                    borderBottom: '5px solid green'
                }
            }>Mis estilos en style</p>
        </>
    )
}