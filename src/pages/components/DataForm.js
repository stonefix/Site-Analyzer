import React from 'react'

export default function DataForm() {
  return (
    <form className='email-form'>
        <input className='custom-input' placeholder='Ваше Имя'/>
        <input className='custom-input' placeholder='Email'/>
        <input className='custom-input' placeholder='URL, domain страницы для анализа'/>
        <button className='custom-button'>Получить отчет</button>
    </form>

  )
}
