import { motion } from "framer-motion";

const Home = () => {
  return (
    <div className="bg-gray-900 min-h-screen text-gray-100">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="text-center py-24 px-4"
      >
        <h1 className="text-5xl font-bold bg-gradient-to-r from-emerald-400 to-blue-500 text-transparent bg-clip-text">
          Smart Stock Management
        </h1>
        <p className="text-gray-400 mt-4 text-xl max-w-2xl mx-auto">
          Unleash the power of intelligent trading with real-time insights and AI-powered recommendations
        </p>
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="bg-emerald-600 text-white px-8 py-3 rounded-lg mt-8 text-lg font-semibold hover:bg-emerald-700 transition-colors"
        >
          Get Started
        </motion.button>
      </motion.div>

      {/* Features Section */}
      <motion.div
        initial="hidden"
        animate="visible"
        variants={{
          hidden: { opacity: 0, y: 30 },
          visible: {
            opacity: 1,
            y: 0,
            transition: { staggerChildren: 0.2, duration: 0.6 }
          },
        }}
        className="grid grid-cols-1 md:grid-cols-3 gap-8 px-8 md:px-16 mb-16"
      >
        {[
          { 
            title: "Real-time Analytics", 
            desc: "Advanced charts and indicators for informed decisions",
            icon: "📊"
          },
          { 
            title: "AI Assistant", 
            desc: "Get intelligent insights and personalized recommendations",
            icon: "🤖"
          },
          { 
            title: "Smart Alerts", 
            desc: "Stay ahead with instant notifications on market movements",
            icon: "🔔"
          },
        ].map((feature, index) => (
          <motion.div
            key={index}
            variants={{ hidden: { opacity: 0, y: 30 }, visible: { opacity: 1, y: 0 } }}
            className="bg-gray-800 p-8 rounded-xl shadow-lg hover:shadow-emerald-500/10 transition-shadow"
          >
            <div className="text-4xl mb-4">{feature.icon}</div>
            <h3 className="text-xl font-bold text-emerald-400">{feature.title}</h3>
            <p className="text-gray-400 mt-2">{feature.desc}</p>
          </motion.div>
        ))}
      </motion.div>

      {/* Trending Stocks */}
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="px-8 md:px-16 pb-16"
      >
        <h2 className="text-3xl font-bold mb-8 text-emerald-400">Trending Stocks</h2>
        <motion.div
          className="grid grid-cols-1 md:grid-cols-3 gap-8"
          initial="hidden"
          animate="visible"
          variants={{
            hidden: { opacity: 0, y: 30 },
            visible: {
              opacity: 1,
              y: 0,
              transition: { staggerChildren: 0.2, duration: 0.6 }
            },
          }}
        >
          {[
            { name: "Apple Inc.", symbol: "NASDAQ: AAPL", price: "$198.45", change: "+2.3%" },
            { name: "Microsoft", symbol: "NASDAQ: MSFT", price: "$402.12", change: "+1.2%" },
            { name: "Alphabet", symbol: "NASDAQ: GOOG", price: "$142.89", change: "+1.5%" },
          ].map((stock, index) => (
            <motion.div
              key={index}
              variants={{ hidden: { opacity: 0, y: 30 }, visible: { opacity: 1, y: 0 } }}
              whileHover={{ scale: 1.03 }}
              className="bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-emerald-500/10 transition-shadow"
            >
              <div>
                <h4 className="text-xl font-bold text-emerald-400">{stock.name}</h4>
                <p className="text-gray-400">{stock.symbol}</p>
                <div className="mt-4 flex items-baseline">
                  <p className="text-2xl font-bold">{stock.price}</p>
                  <span className="ml-2 text-emerald-400">{stock.change}</span>
                </div>
              </div>
            </motion.div>
          ))}
        </motion.div>
      </motion.div>

      {/* Market Stats Banner */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="bg-gray-800 py-8 px-8 md:px-16"
      >
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {[
            { label: "Market Cap", value: "$2.8T" },
            { label: "24h Volume", value: "$86.2B" },
            { label: "Active Traders", value: "2.4M+" },
            { label: "Daily Trades", value: "890K+" },
          ].map((stat, index) => (
            <div key={index} className="text-center">
              <p className="text-3xl font-bold text-emerald-400">{stat.value}</p>
              <p className="text-gray-400 mt-1">{stat.label}</p>
            </div>
          ))}
        </div>
      </motion.div>
    </div>
  );
};

export default Home;