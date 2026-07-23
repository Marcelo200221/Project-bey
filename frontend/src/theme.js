import { ref } from 'vue'

const currentTheme = ref(localStorage.getItem('theme') || 'light')
const isLowPower = ref(localStorage.getItem('low_power') === 'true')

export function useTheme() {
  const setTheme = (newTheme) => {
    currentTheme.value = newTheme
    localStorage.setItem('theme', newTheme)
    if (newTheme === 'dark') {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }

  const setLowPower = (value) => {
    isLowPower.value = value
    localStorage.setItem('low_power', value ? 'true' : 'false')
    if (value) {
      document.documentElement.classList.add('low-power')
    } else {
      document.documentElement.classList.remove('low-power')
    }
  }

  const initTheme = () => {
    setTheme(currentTheme.value)
    setLowPower(isLowPower.value)
  }

  return {
    theme: currentTheme,
    setTheme,
    lowPower: isLowPower,
    setLowPower,
    initTheme
  }
}

