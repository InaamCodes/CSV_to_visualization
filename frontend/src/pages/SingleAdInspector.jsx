import { useState } from 'react';
import { scrapeSingle } from '../api';

function SingleAdInspector() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [productData, setProductData] = useState(null);
  const [error, setError] = useState(null);
  const [selectedImage, setSelectedImage] = useState(0);

  const handleAnalyze = async () => {
    if (!url) {
      setError('Please enter a URL');
      return;
    }

    setLoading(true);
    setError(null);
    setProductData(null);
    
    try {
      const result = await scrapeSingle(url);
      setProductData(result.data);
      setSelectedImage(0);
    } catch (err) {
      console.error('Error scraping:', err);
      setError(err.response?.data?.detail || 'Failed to scrape the URL. Please check if it is a valid ikman.lk ad page.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Single Ad Inspector</h2>
        <p className="text-gray-600 mb-4">
          Paste a specific ikman.lk ad URL to analyze it in detail
        </p>
        
        {/* Input Section */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Ad URL
            </label>
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleAnalyze()}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent text-lg"
              placeholder="https://ikman.lk/en/ad/..."
            />
          </div>
          
          <button
            onClick={handleAnalyze}
            disabled={loading}
            className={`w-full md:w-auto px-8 py-3 rounded-lg font-semibold text-white transition-colors ${
              loading 
                ? 'bg-gray-400 cursor-not-allowed' 
                : 'bg-primary-600 hover:bg-primary-700'
            }`}
          >
            {loading ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Analyzing...
              </span>
            ) : (
              '🔍 Analyze Ad'
            )}
          </button>
        </div>

        {/* Error Message */}
        {error && (
          <div className="mt-4 p-4 bg-red-100 text-red-800 rounded-lg">
            {error}
          </div>
        )}
      </div>

      {/* Product Card */}
      {productData && (
        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          <div className="md:flex">
            {/* Image Gallery */}
            <div className="md:w-1/2 bg-gray-100">
              {productData.images && productData.images.length > 0 ? (
                <div className="space-y-4 p-6">
                  {/* Main Image */}
                  <div className="aspect-w-16 aspect-h-12 bg-white rounded-lg overflow-hidden">
                    <img
                      src={productData.images[selectedImage]}
                      alt={productData.title}
                      className="w-full h-96 object-contain"
                    />
                  </div>
                  
                  {/* Thumbnail Gallery */}
                  {productData.images.length > 1 && (
                    <div className="flex space-x-2 overflow-x-auto">
                      {productData.images.map((img, idx) => (
                        <button
                          key={idx}
                          onClick={() => setSelectedImage(idx)}
                          className={`flex-shrink-0 w-20 h-20 rounded-lg overflow-hidden border-2 transition-all ${
                            selectedImage === idx 
                              ? 'border-primary-500 shadow-md' 
                              : 'border-transparent hover:border-gray-300'
                          }`}
                        >
                          <img
                            src={img}
                            alt={`Thumbnail ${idx + 1}`}
                            className="w-full h-full object-cover"
                          />
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              ) : (
                <div className="h-96 flex items-center justify-center">
                  <div className="text-gray-400 text-center">
                    <svg className="mx-auto h-12 w-12 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                    <p>No image available</p>
                  </div>
                </div>
              )}
            </div>

            {/* Product Details */}
            <div className="md:w-1/2 p-8">
              {/* Title */}
              <h1 className="text-3xl font-bold text-gray-900 mb-4">
                {productData.title}
              </h1>

              {/* Price */}
              <div className="mb-6">
                <div className="text-5xl font-bold text-green-600">
                  {productData.price ? `Rs ${productData.price.toLocaleString()}` : 'Price not available'}
                </div>
              </div>

              {/* Location Badge */}
              <div className="mb-6">
                <span className="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-primary-100 text-primary-800">
                  <svg className="mr-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  {productData.location}
                </span>
              </div>

              {/* Seller Info */}
              <div className="mb-6 p-4 bg-gray-50 rounded-lg">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <div className="h-10 w-10 rounded-full bg-primary-200 flex items-center justify-center">
                      <svg className="h-6 w-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      </svg>
                    </div>
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-700">Seller</p>
                    <p className="text-sm text-gray-900 font-semibold">{productData.seller_name}</p>
                  </div>
                </div>
              </div>

              {/* Description */}
              <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-900 mb-3">Description</h3>
                <div className="prose prose-sm text-gray-700 bg-gray-50 p-4 rounded-lg">
                  <p className="whitespace-pre-line">{productData.description}</p>
                </div>
              </div>

              {/* View Original Button */}
              <a
                href={productData.url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-primary-600 hover:bg-primary-700 transition-colors"
              >
                View on ikman.lk
                <svg className="ml-2 -mr-1 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      )}

      {/* Example URLs Section */}
      {!productData && !loading && (
        <div className="bg-blue-50 rounded-lg p-6">
          <h3 className="text-lg font-semibold text-blue-900 mb-3">💡 Example URLs</h3>
          <p className="text-blue-800 mb-2">Try pasting a URL from any ikman.lk ad page, such as:</p>
          <ul className="list-disc list-inside text-blue-700 space-y-1 text-sm">
            <li>Electronics: https://ikman.lk/en/ad/...</li>
            <li>Vehicles: https://ikman.lk/en/ad/...</li>
            <li>Real Estate: https://ikman.lk/en/ad/...</li>
          </ul>
        </div>
      )}
    </div>
  );
}

export default SingleAdInspector;
