import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import SingleAdInspector from './pages/SingleAdInspector';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        {/* Navigation */}
        <nav className="bg-white shadow-md">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex space-x-8">
                <Link 
                  to="/" 
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 border-b-2 border-transparent hover:border-primary-500 transition-colors"
                >
                  📊 Dashboard
                </Link>
                <Link 
                  to="/inspector" 
                  className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900 border-b-2 border-transparent hover:border-primary-500 transition-colors"
                >
                  🔍 Ad Inspector
                </Link>
              </div>
              <div className="flex items-center">
                <h1 className="text-xl font-bold text-primary-600">Ikman.lk Scraper</h1>
              </div>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/inspector" element={<SingleAdInspector />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
