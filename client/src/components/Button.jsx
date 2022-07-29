import React from 'react'

export default function Button({onClick, text, loading}) {
  if (!loading) {
    return (
      <button className='button' onClick={onClick}>{text}</button>
    )
  } else {
    return (
      <button className='button' disabled={true} onClick={() => {}}>Loading...</button>
    )
  }
}