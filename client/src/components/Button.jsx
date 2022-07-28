import React from 'react'
import { useState } from 'react'

export default function Button({onClick, text, loading}) {
  if (!loading) {
    return (
      <button className='button' onClick={onClick}>{text}</button>
    )
  } else {
    return (
      <button className='button' onClick={() => {}}>Loading...</button>
    )
  }
}