import React, { useState, useEffect } from 'react';
import './App.css';

// Componente funcional que muestra las características de React
const ReactFeatures: React.FC = () => {
  const [count, setCount] = useState(0);
  const [inputValue, setInputValue] = useState('');
  const [showInfo, setShowInfo] = useState(false);

  // useEffect para efectos secundarios
  useEffect(() => {
    document.title = `React App - Counter: ${count}`;
  }, [count]);

  const handleIncrement = () => {
    setCount(prevCount => prevCount + 1);
  };

  const handleDecrement = () => {
    setCount(prevCount => prevCount - 1);
  };

  return (
    <div className="feature-card">
      <h3>React Features</h3>
      <div className="feature-item">
        <h4>🎯 Hooks (useState)</h4>
        <p>Counter: {count}</p>
        <button onClick={handleIncrement}>+</button>
        <button onClick={handleDecrement}>-</button>
      </div>
      
      <div className="feature-item">
        <h4>📝 Events and State</h4>
        <input 
          type="text" 
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Write something..."
        />
        <p>Text: {inputValue}</p>
      </div>

      <div className="feature-item">
        <h4>⚡ useEffect</h4>
        <button onClick={() => setShowInfo(!showInfo)}>
          {showInfo ? 'Hide' : 'Show'} information
        </button>
        {showInfo && (
          <div className="info-box">
            <p>This text appears/disappears using useEffect</p>
            <p>The page title also changes with the counter</p>
          </div>
        )}
      </div>
    </div>
  );
};

// Interfaz para los datos del clima
interface WeatherData {
  name: string;
  main: {
    temp: number;
    feels_like: number;
    humidity: number;
    pressure: number;
  };
  weather: Array<{
    main: string;
    description: string;
    icon: string;
  }>;
  wind: {
    speed: number;
  };
  sys: {
    country: string;
  };
}

// Componente de consulta de clima
const WeatherApp: React.FC = () => {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const [searchCount, setSearchCount] = useState<number>(0);
  const [apiKey, setApiKey] = useState('');
  const [showApiInstructions, setShowApiInstructions] = useState(false);

  const API_URL = 'https://api.openweathermap.org/data/2.5/weather';

  const fetchWeather = async (cityName: string) => {
    // Validación mejorada de la API key
    const trimmedApiKey = apiKey.trim();
    if (!trimmedApiKey) {
      setError('Please enter your OpenWeatherMap API key first');
      return;
    }

    if (searchCount >= 5) {
      setError('You have reached the maximum of 5 searches per session. Reload the page to search more.');
      return;
    }

    setLoading(true);
    setError(null);
    setSearchCount(prev => prev + 1);

    try {
      console.log('Fetching weather for:', cityName);
      console.log('API Key length:', trimmedApiKey.length);
      
      const response = await fetch(
        `${API_URL}?q=${encodeURIComponent(cityName)}&appid=${trimmedApiKey}&units=metric&lang=en`
      );
      
      console.log('Response status:', response.status);
      
      if (!response.ok) {
        if (response.status === 401) {
          throw new Error('Invalid API key. Please check your OpenWeatherMap API key.');
        } else if (response.status === 404) {
          throw new Error('City not found. Please check the spelling.');
        } else {
          throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
      }
      
      const data: WeatherData = await response.json();
      console.log('Weather data received:', data.name);
      setWeatherData(data);
      
      // Agregar a historial
      if (!searchHistory.includes(cityName)) {
        setSearchHistory(prev => [cityName, ...prev.slice(0, 4)]);
      }
    } catch (err) {
      console.error('Error fetching weather:', err);
      setError(err instanceof Error ? err.message : 'Error getting data');
      setWeatherData(null);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    const trimmedCity = city.trim();
    if (trimmedCity && apiKey.trim()) {
      fetchWeather(trimmedCity);
    } else if (!apiKey.trim()) {
      setError('Please enter your OpenWeatherMap API key first');
    } else if (!trimmedCity) {
      setError('Please enter a city name');
    }
  };

  const handleHistoryClick = (cityName: string) => {
    setCity(cityName);
    fetchWeather(cityName);
  };

  const handleApiKeyChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setApiKey(value);
    // Limpiar error si el usuario está ingresando la API key
    if (error && value.trim()) {
      setError(null);
    }
  };

  const clearApiKey = () => {
    setApiKey('');
    setError(null);
    setWeatherData(null);
  };

  const getWeatherIcon = (iconCode: string) => {
    return `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
  };

  const getWeatherDescription = (weatherId: number) => {
    const descriptions: { [key: number]: string } = {
      200: 'Thunderstorm with light rain',
      201: 'Thunderstorm with rain',
      202: 'Thunderstorm with heavy rain',
      300: 'Light drizzle',
      301: 'Drizzle',
      500: 'Light rain',
      501: 'Moderate rain',
      502: 'Heavy rain',
      600: 'Light snow',
      601: 'Snow',
      602: 'Heavy snow',
      700: 'Mist',
      800: 'Clear sky',
      801: 'Few clouds',
      802: 'Scattered clouds',
      803: 'Broken clouds',
      804: 'Overcast clouds'
    };
    return descriptions[weatherId] || 'Unknown condition';
  };

  return (
    <div className="weather-app">
      <h3>🌤️ Weather App</h3>
      
      <div className="api-instructions">
        <h4>📋 How to use this Weather App:</h4>
        <ol>
          <li>Get your free API key from <a href="https://openweathermap.org/api" target="_blank" rel="noopener noreferrer">OpenWeatherMap</a></li>
          <li>Sign up for a free account</li>
          <li>Go to "My API keys" section</li>
          <li>Copy your API key and paste it below</li>
          <li>Enter any city name and search!</li>
        </ol>
        <button 
          onClick={() => setShowApiInstructions(!showApiInstructions)}
          className="toggle-instructions-btn"
        >
          {showApiInstructions ? 'Hide' : 'Show'} API Key Instructions
        </button>
      </div>

      {showApiInstructions && (
        <div className="api-key-section">
          <h4>🔑 Enter your OpenWeatherMap API Key:</h4>
          <div className="api-input-group">
            <input
              type="password"
              value={apiKey}
              onChange={handleApiKeyChange}
              placeholder="Paste your API key here..."
              className="api-key-input"
            />
            <button 
              onClick={clearApiKey}
              className="clear-api-btn"
              title="Clear API key"
            >
              🗑️
            </button>
          </div>
          <p className="api-note">
            <strong>Note:</strong> Your API key is stored only in your browser and is not sent to any server except OpenWeatherMap.
          </p>
        </div>
      )}
      
      <form onSubmit={handleSearch} className="weather-form">
        <div className="input-group">
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter any city name in the world..."
            className="city-input"
            disabled={!apiKey.trim()}
          />
          <button 
            type="submit" 
            disabled={loading || !city.trim() || !apiKey.trim()}
          >
            {loading ? '🔍 Searching...' : '🔍 Search'}
          </button>
        </div>
        <p className="venezuela-info">
          🌎 You can search any city in the world.<br/>
          Remaining searches: {5 - searchCount}
          {!apiKey.trim() && (
            <>
              <br/>
              <span className="api-warning">⚠️ Please enter your API key first</span>
            </>
          )}
        </p>
      </form>

      {searchHistory.length > 0 && (
        <div className="search-history">
          <h4>📋 Search history:</h4>
          <div className="history-buttons">
            {searchHistory.map((cityName, index) => (
              <button
                key={index}
                onClick={() => handleHistoryClick(cityName)}
                className="history-btn"
              >
                {cityName}
              </button>
            ))}
          </div>
        </div>
      )}

      {error && (
        <div className="error-message">
          ❌ {error}
        </div>
      )}

      {weatherData && (
        <div className="weather-card">
          <div className="weather-header">
            <h4>{weatherData.name}, {weatherData.sys.country}</h4>
            <img 
              src={getWeatherIcon(weatherData.weather[0].icon)} 
              alt={weatherData.weather[0].description}
              className="weather-icon"
            />
          </div>
          
          <div className="weather-info">
            <div className="temperature">
              <span className="temp-value">{Math.round(weatherData.main.temp)}°C</span>
              <span className="temp-feels">Feels like: {Math.round(weatherData.main.feels_like)}°C</span>
            </div>
            
            <div className="weather-description">
              {getWeatherDescription(parseInt(weatherData.weather[0].icon.slice(0, -1)))}
            </div>
            
            <div className="weather-details">
              <div className="detail-item">
                <span className="detail-label">💧 Humidity:</span>
                <span className="detail-value">{weatherData.main.humidity}%</span>
              </div>
              <div className="detail-item">
                <span className="detail-label">🌬️ Wind:</span>
                <span className="detail-value">{weatherData.wind.speed} m/s</span>
              </div>
              <div className="detail-item">
                <span className="detail-label">📊 Pressure:</span>
                <span className="detail-value">{weatherData.main.pressure} hPa</span>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

// Componente de comparación entre frameworks
const FrameworkComparison: React.FC = () => {
  const [selectedFramework, setSelectedFramework] = useState<'react' | 'vue' | 'angular'>('react');

  const frameworks = {
    react: {
      name: 'React',
      type: 'UI Library',
      company: 'Meta (Facebook)',
      language: 'JavaScript + JSX',
      learning: 'Medium',
      pros: ['Virtual DOM', 'Large ecosystem', 'Flexibility', 'React Native'],
      cons: ['Not a complete framework', 'Complex ecosystem learning curve'],
      code: `// React - Hooks
const [count, setCount] = useState(0);
const increment = () => setCount(count + 1);

return (
  <div>
    <p>Counter: {count}</p>
    <button onClick={increment}>+</button>
  </div>
);`
    },
    vue: {
      name: 'Vue.js',
      type: 'Progressive Framework',
      company: 'Community',
      language: 'JavaScript + Templates',
      learning: 'Low',
      pros: ['Low learning curve', 'Progressive adoption', 'Intuitive syntax', 'Official ecosystem'],
      cons: ['Less corporate backing', 'Smaller community'],
      code: `<!-- Vue - Composition API -->
<script setup>
const count = ref(0);
const increment = () => count.value++;
</script>

<template>
  <div>
    <p>Counter: {{ count }}</p>
    <button @click="increment">+</button>
  </div>
</template>`
    },
    angular: {
      name: 'Angular',
      type: 'Complete Framework',
      company: 'Google',
      language: 'TypeScript',
      learning: 'High',
      pros: ['Complete framework', 'TypeScript', 'Powerful CLI', 'Dependency injection'],
      cons: ['High learning curve', 'More verbose', 'Less flexible'],
      code: `// Angular - Signals
@Component({
  selector: 'app-counter',
  template: \`
    <div>
      <p>Counter: {{ count() }}</p>
      <button (click)="increment()">+</button>
    </div>
  \`
})
export class CounterComponent {
  count = signal(0);
  increment() {
    this.count.update(value => value + 1);
  }
}`
    }
  };

  const currentFramework = frameworks[selectedFramework];

  return (
    <div className="comparison-section">
      <h3>🔄 Framework Comparison</h3>
      
      <div className="framework-selector">
        <button 
          className={selectedFramework === 'react' ? 'active' : ''}
          onClick={() => setSelectedFramework('react')}
        >
          React
        </button>
        <button 
          className={selectedFramework === 'vue' ? 'active' : ''}
          onClick={() => setSelectedFramework('vue')}
        >
          Vue.js
        </button>
        <button 
          className={selectedFramework === 'angular' ? 'active' : ''}
          onClick={() => setSelectedFramework('angular')}
        >
          Angular
        </button>
      </div>

      <div className="framework-details">
        <div className="framework-info">
          <h4>{currentFramework.name}</h4>
          <div className="info-grid">
            <div><strong>Type:</strong> {currentFramework.type}</div>
            <div><strong>Company:</strong> {currentFramework.company}</div>
            <div><strong>Language:</strong> {currentFramework.language}</div>
            <div><strong>Learning curve:</strong> {currentFramework.learning}</div>
          </div>
        </div>

        <div className="pros-cons">
          <div className="pros">
            <h5>✅ Advantages</h5>
            <ul>
              {currentFramework.pros.map((pro, index) => (
                <li key={index}>{pro}</li>
              ))}
            </ul>
          </div>
          <div className="cons">
            <h5>❌ Disadvantages</h5>
            <ul>
              {currentFramework.cons.map((con, index) => (
                <li key={index}>{con}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="code-example">
          <h5>💻 Code Example</h5>
          <pre>{currentFramework.code}</pre>
        </div>
      </div>
    </div>
  );
};

// Componente principal
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 React - Educational Framework</h1>
        <p>Application that demonstrates the main features of React</p>
      </header>
      
      <main className="App-main">
        <div className="framework-info">
          <h2>What is React?</h2>
          <ul>
            <li>📦 JavaScript library for user interfaces</li>
            <li>⚛️ Reusable components</li>
            <li>🔄 Reactive state</li>
            <li>🎣 Hooks for state logic</li>
            <li>⚡ Virtual DOM for performance</li>
            <li>🎯 "Learn once, write anywhere"</li>
          </ul>
        </div>

        <ReactFeatures />

        <WeatherApp />

        <FrameworkComparison />

        <div className="code-example">
          <h3>React Code Example</h3>
          <pre>
{`function Component() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Counter: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}`}
          </pre>
        </div>
      </main>
    </div>
  );
}

export default App;
