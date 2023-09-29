import React from 'react'

export default function Hero() {
  return (
    <div className='hero'>
    <div className='hero__info'>
        <img  className="hero__icon" src='../hero-icon.png'/>
        <span className='header'>Анализ успеха конкурентов с ML и SEO</span>
        <span className='subheader'>Вам когда-нибудь хотелось быстро и точно понимать, о чем тот или иной сайт или быстро изучить сайты всех конкурентов?</span>
        <button className='custom-button'>Узнать детали -{">"}</button>

    </div>
    <img className='hero__image' src='../hero-image.png'/>
    </div>
  )
}
