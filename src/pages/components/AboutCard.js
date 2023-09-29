import React from 'react'

export default function AboutCard({image,header,subheader}) {
  return (
    <div className='card'>
      <div className='card__img'>
      <img src={image}/>

      </div>
      <span className='card__header'>Lorem ipsum dolor sit 
      </span>
      <span className='card_sub'>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna l</span>
      
    </div>
  )
}
