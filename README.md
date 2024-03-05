<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Encryption Program</title>
</head>
<body>
    <h1>Encryption Program</h1>

    <p>This Python script allows you to encrypt and decrypt files using a simple encryption algorithm.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Key Generation:</strong> Generate a new encryption key.</li>
        <li><strong>Encryption:</strong> Encrypt files using the generated key.</li>
        <li><strong>Decryption:</strong> Decrypt files using the generated key.</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>os</code> module</li>
        <li><code>random</code> module</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li>Clone or download the repository to your local machine.</li>
        <li>Open a terminal and navigate to the directory containing the script.</li>
        <li>Use the following command to run the script:</li>
    </ol>
    <code>python encryption_program.py [mode] [key_name]</code>

    <p>Replace <code>[mode]</code> with one of the following:</p>
    <ul>
        <li><code>newkey</code>: Generate a new encryption key.</li>
        <li><code>encrypt</code>: Encrypt files using an existing key.</li>
        <li><code>decrypt</code>: Decrypt files using an existing key.</li>
    </ul>

    <p>Replace <code>[key_name]</code> with the name of the key (without the <code>.key</code> extension).</p>

    <h2>Key Management</h2>
    <ul>
        <li>Keys are stored in the <code>keys</code> folder within the same directory as the script.</li>
        <li>Encrypted files are stored in the <code>target</code> folder within the same directory as the script.</li>
        <li>Decrypted files will overwrite the original files in the <code>target</code> folder.</li>
    </ul>

    <h2>Example Usage</h2>

    <h3>Generate a New Key</h3>
    <pre><code>python encryption_program.py newkey my_key</code></pre>

    <h3>Encrypt Files</h3>
    <pre><code>python encryption_program.py encrypt my_key</code></pre>

    <h3>Decrypt Files</h3>
    <pre><code>python encryption_program.py decrypt my_key</code></pre>

    <h2>Notes</h2>
    <ul>
        <li>Make sure to keep your encryption key secure.</li>
        <li>Always remember to back up your files before encryption.</li>
    </ul>
</body>
</html>
