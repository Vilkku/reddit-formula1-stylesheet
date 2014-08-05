<?php

// This file is to be used as a webhook endpoint in GitHub. This means
// you probably have to move this file to another directory for this
// to work.

try {
    $payload = json_decode(file_get_contents('php://input'));
} catch(Exception $e) {
    http_response_code(400);
    exit('invalid payload format');
}

if ($payload->repository->id != '5750416') {
    http_response_code(403);
    exit('invalid github repository id ('.$payload->repository->id.')');
}

if ($payload->ref === 'refs/heads/master') {
    exec('sh ../../../../reddit-formula1-stylesheet/webhook.sh');
}

?>
