section .text
global _start

_start:
  mov rax, -5
  comp rax, 0
  jge done
  neg rax
done:

  mov rax, 60
  xor rdi, rdi
  syscall
