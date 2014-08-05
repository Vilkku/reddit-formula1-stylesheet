<?php

// This file is to be used as a webhook endpoint in GitHub. This means
// you probably have to move this file to another directory for this
// to work.

$home = '';
$secret = '';

$headers = getallheaders();
$hubSignature = $headers['X-Hub-Signature'];
list($algo, $hash) = explode('=', $hubSignature, 2);

try {
    $payload = file_get_contents('php://input');
    $data = json_decode($payload);
} catch(Exception $e) {
    http_response_code(400);
    exit('invalid payload format');
}

if ($hash !== hash_hmac($algo, $payload, $secret)) {
    http_response_code(403);
    exit('invalid secret');
}

if ($data->ref === 'refs/heads/master') {
    exec('sh '.$home.'/reddit-formula1-stylesheet/webhook.sh');
    exit('success');
}

exit('branch not master, nothing done');

?>
