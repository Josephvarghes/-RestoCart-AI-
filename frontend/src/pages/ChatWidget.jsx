import { useState, useEffect, useRef, useCallback } from "react";
import ReactMarkdown from "react-markdown";
import toast from "react-hot-toast";
import { MessageCircle, X } from "lucide-react";

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState("");
  const messagesEndRef = useRef(null);

  const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, []);

  const fetchHistory = useCallback(async () => {
    if (!sessionId) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/v1/ai/history/${sessionId}`);
      if (res.ok) {
        const data = await res.json();
        setMessages(data);
      }
    } catch (err) {
      console.error("Failed to fetch chat history:", err);
    }
  }, [API_BASE_URL, sessionId]);

  useEffect(() => {
    let id = localStorage.getItem("chat_session_id");
    if (!id) {
      id = crypto.randomUUID ? crypto.randomUUID() : Math.random().toString(36).substring(2, 11);
      localStorage.setItem("chat_session_id", id);
    }
    setSessionId(id);
  }, []);

  useEffect(() => {
    fetchHistory();
  }, [fetchHistory]);

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading, scrollToBottom]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/v1/ai/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          question: input,
          session_id: sessionId
        }),
      });

      const data = await res.json();
      
      let finalAnswer = data.answer;
      
      // Check for the deterministic tag indicating a successful order
      if (finalAnswer.includes("[ORDER_SUCCESS]")) {
        toast.success("🎉 Order placed successfully via AI!", {
          duration: 5000,
          position: "top-center"
        });
        
        // Remove the tag so the user doesn't see it in the chat bubble
        finalAnswer = finalAnswer.replace("[ORDER_SUCCESS]", "").trim();
      }

      const aiMessage = { role: "assistant", content: finalAnswer };
      setMessages((prev) => [...prev, aiMessage]);

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Sorry, I couldn't reach the AI right now." },
      ]);
      toast.error("Failed to connect to the AI Assistant.");
    } finally {
      setIsLoading(false);
    }
  };

  const toggleChat = () => setIsOpen(!isOpen);

  return (
    <>
      <button
        onClick={toggleChat}
        className="fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:bg-blue-700 hover:scale-105 transition-all duration-300 z-50 flex items-center justify-center"
      >
        {isOpen ? <X size={24} /> : <MessageCircle size={24} />}
      </button>

      <div
        className={`fixed bottom-24 right-6 w-96 h-[550px] bg-white rounded-2xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-gray-100 flex flex-col transform transition-all duration-300 origin-bottom-right z-40 ${
          isOpen ? "scale-100 opacity-100" : "scale-0 opacity-0 pointer-events-none"
        }`}
      >
        <div className="p-4 border-b border-gray-100 flex justify-between items-center bg-white/80 backdrop-blur-md rounded-t-2xl">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <h3 className="font-bold text-slate-800">AI Assistant</h3>
          </div>
          <button onClick={toggleChat} className="text-slate-400 hover:text-slate-600 transition-colors">
            <X size={20} />
          </button>
        </div>

        <div className="p-4 flex-1 overflow-y-auto space-y-4 bg-slate-50">
          {messages.length === 0 && !isLoading && (
            <div className="text-center text-slate-400 mt-20">
              <MessageCircle size={48} className="mx-auto mb-2 opacity-50" />
              <p>Ask me about the menu or place an order!</p>
            </div>
          )}
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`p-3 rounded-2xl max-w-[85%] shadow-sm text-sm ${
                msg.role === "user"
                  ? "bg-blue-600 text-white ml-auto rounded-br-none"
                  : "bg-white text-slate-700 border border-gray-100 rounded-bl-none"
              }`}
            >
              {msg.role === "assistant" ? (
                <div className="prose prose-sm prose-slate max-w-none">
                  <ReactMarkdown>{msg.content}</ReactMarkdown>
                </div>
              ) : (
                msg.content
              )}
            </div>
          ))}
          {isLoading && (
            <div className="p-3 bg-white border border-gray-100 rounded-2xl rounded-bl-none max-w-[85%] shadow-sm flex items-center gap-1 w-16">
              <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
              <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
              <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-gray-100 rounded-b-2xl">
          <div className="flex gap-2 bg-slate-50 rounded-xl p-1 border border-gray-200 focus-within:border-blue-400 focus-within:ring-2 focus-within:ring-blue-100 transition-all">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Type a message..."
              className="flex-1 bg-transparent px-3 py-2 text-sm focus:outline-none text-slate-700"
            />
            <button
              onClick={sendMessage}
              disabled={!input.trim() || isLoading}
              className="bg-blue-600 text-white px-4 py-2 rounded-lg disabled:opacity-50 hover:bg-blue-700 transition-colors text-sm font-medium"
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
