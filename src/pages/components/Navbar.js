import React from 'react'
import Link from 'next/link'
export default function Navbar() {
  return (
    <nav className='align'>
        <div className='nav__logo align'>
            <img src='../rocket.png' className='logo_image'/>
            <span className='logo_title'>SEOInsight</span>
        </div>
        <div className='nav__links align'>
            <Link href="#" className='link'>Главная</Link>
            <Link href="#" className='link'>Услуги</Link>
            <Link href="#" className='link'>Контакты</Link>
        </div>
    </nav>
  )
}
