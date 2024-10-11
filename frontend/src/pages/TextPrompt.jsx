import React, { useState } from 'react';
import './TextPrompt.css';  // Importing the TextPrompt-specific CSS

const TextPrompt = () => {
  const [textPrompt, setTextPrompt] = useState('');
  const [submittedPrompt, setSubmittedPrompt] = useState('');

  const handleTextPromptChange = (e) => {
    setTextPrompt(e.target.value);
  };

  const handleSubmit = () => {
    if (textPrompt.trim() !== '') {
      setSubmittedPrompt(textPrompt);
      setTextPrompt(''); // Clear input after submission
    }
  };

  return (
    <div className="text-prompt-container">
      <h2>Task as a Text Prompt</h2>
      <p>Provide a detailed description of the task.</p>
      <div className="input-group">
        <textarea
          value={textPrompt}
          onChange={handleTextPromptChange}
          rows="5"
          placeholder="Enter a task description"
          className="text-prompt-input"
        ></textarea>
        <button onClick={handleSubmit} className="submit-button">Submit</button>
      </div>
      {submittedPrompt && (
        <div className="submitted-prompt">
          <h3>Submitted Prompt:</h3>
          <p>{submittedPrompt}</p>
        </div>
      )}
    </div>
  );
};

export default TextPrompt;