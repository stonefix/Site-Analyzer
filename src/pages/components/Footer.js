import React from 'react'
import Link from 'next/link'
export default function Footer() {
  return (
    <footer>
      <div className='footer__info'>
        <img src='../phone.png'></img>
        <div className='footer__info--text'>
        <span>Пн-Пт 9.00-18.00</span>
        <span>+37529637828</span>
        </div>
      
      </div>
      <div className='footer__info'>
        <img src='../gmail.png'></img>
        <div className='footer__info--text'>
        <span>У вас есть вопросы?</span>
        <span>seoinsight@gmail.com</span>
        </div>
      </div>
      <hr/>
      <div className='copyright'>
      <span>Copyright © 2022 Company.com . All rights reserved.</span>
      <div className='nav__links align'>
            <Link href="#" className='link'>Главная</Link>
            <Link href="#" className='link'>Услуги</Link>
            <Link href="#" className='link'>Контакты</Link>
        </div>
      </div>
    </footer>
  )
}
