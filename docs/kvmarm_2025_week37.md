# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:55:21

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 227
- **总 Thread 数**: 40
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 34 threads (209 邮件)
- **RFC**: 1 threads (6 邮件)
- **Bug Report**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Other**: 3 threads (8 邮件)

---

## 📌 PATCH

共 34 个 thread

---

### Thread 1: [PATCH v6 02/24] ring-buffer: Introduce ring-buffer remotes

**📧 邮件数**: 22 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 8 Sep 2025 19:13:43 -0400

#### 🤖 AI 总结

本邮件讨论的主题是关于引入环形缓冲区远程功能的补丁（PATCH v6 02/24）。该补丁旨在增强 Linux 内核的环形缓冲区，以支持远程数据写入。

在历史讨论中，参与者们对补丁的命名和实现细节进行了探讨，特别是关于内存分配和锁机制的使用。Steven Rostedt 提出了对函数命名的建议，认为如果涉及内存分配，函数名中应包含“alloc”字样。此外，他还建议在实现中使用更简洁的锁定机制，以避免不必要的解锁操作。

在本周的新讨论中，主要集中在补丁的具体实现和代码风格上。Vincent Donnefort 和 Steven Rostedt 继续讨论了代码中的一些细节，例如是否需要增加对分配大小的检查，以及如何处理环形缓冲区的页顺序问题。Rostedt 强调了代码注释的重要性，认为应在函数中添加详细的说明，以便于理解参数的用途和要求。此外，讨论中还涉及到如何处理用户接口，以避免用户在使用时产生困惑。

总体来看，本周的讨论主要集中在补丁的实现细节、代码可读性和用户体验上，参与者们积极提出建议以改进补丁的质量。

#### 📝 邮件列表

1. **[09-08 19:13]** Re: [PATCH v6 02/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
2. **[09-08 19:36]** Re: [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
3. **[09-08 19:37]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
4. **[09-09 13:08]** Re: [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[09-09 13:10]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[09-09 09:38]** Re: [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
7. **[09-09 09:40]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
8. **[09-09 17:10]** Re: [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[09-09 17:14]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[09-09 14:19]** Re: [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
11. **[09-09 14:39]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
12. **[09-09 14:52]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
13. **[09-09 17:47]** Re: [PATCH v6 06/24] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
14. **[09-09 17:52]** Re: [PATCH v6 07/24] tracing: Add events/ root files to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
15. **[09-09 18:24]** Re: [PATCH v6 06/24] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
16. **[09-09 18:26]** Re: [PATCH v6 10/24] tracing: Introduce simple_ring_buffer
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
17. **[09-10 10:45]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[09-10 10:47]** Re: [PATCH v6 10/24] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[09-10 12:45]** Re: [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
20. **[09-10 12:47]** Re: [PATCH v6 15/24] KVM: arm64: Support unaligned fixmap in the
 pKVM hyp
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
21. **[09-10 18:06]** Re: [PATCH v6 15/24] KVM: arm64: Support unaligned fixmap in the
 pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[09-12 14:48]** Re: [PATCH v6 16/24] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 2: [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on
 panic

**📧 邮件数**: 17 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 8 Sep 2025 13:11:15 +0100

#### 🤖 AI 总结

本邮件线程主要讨论了针对 KVM (Kernel-based Virtual Machine) 的两个补丁和相关问题。

1. **原始补丁内容**：
   - 补丁 [PATCH 2/2] 提议将 hyp 代码映射为只读，并在发生 panic 时转储指令。这一补丁旨在提高系统的稳定性和调试能力。

2. **之前的讨论要点**：
   - 之前的讨论集中在补丁 [PATCH 1/2] 上，主要关注在 hyp panic 时转储指令的实现。参与者 Will Deacon 提出了对函数命名和参数检查的建议，以防止潜在的用户空间调用问题。

3. **本周的新讨论与进展**：
   - 本周的讨论中，Will Deacon 对补丁表示认可，并表示将根据反馈进行修改。Oliver Upton 提出了两个补丁的回退，理由是之前的调度修复引入了多个问题，决定暂时回退以便后续改进。最终，这两个回退补丁已被应用，标志着对现有问题的快速响应和解决。

此外，Sebastian Ott 提出了关于 KVM PSCI 版本的补丁，旨在支持在不同主机内核版本之间的迁移，确保在迁移过程中能够请求双方都支持的 PSCI 版本。讨论中还涉及了向后迁移的潜在问题及其解决方案。整体来看，本周的讨论显示了对系统稳定性和兼容性的持续关注。

#### 📝 邮件列表

1. **[09-08 13:11]** Re: [PATCH 2/2] KVM: arm64: Map hyp text as RO and dump instr on
 panic
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-08 13:16]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-09 13:10]** Re: [PATCH 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[09-10 11:09]** [PATCH 0/2] KVM: arm64: Revert resched fixes for stage-2 destruction
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-10 11:09]** [PATCH 1/2] Revert "KVM: arm64: Reschedule as needed when destroying the stage-2 page-tables"
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-10 11:09]** [PATCH 2/2] Revert "KVM: arm64: Split kvm_pgtable_stage2_destroy()"
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-10 11:09]** [PATCH] bad bad bad
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-10 11:12]** Re: (subset) [PATCH 0/2] KVM: arm64: Revert resched fixes for stage-2 destruction
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-11 16:49]** [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
10. **[09-11 16:49]** [PATCH 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
11. **[09-11 16:49]** [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
12. **[09-11 16:18]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
13. **[09-11 17:59]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
14. **[09-11 17:02]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
15. **[09-11 18:29]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
16. **[09-11 17:32]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
17. **[09-11 18:46]** Re: [PATCH 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 3: [PATCH v6 00/11] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 15 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 12 Sep 2025 09:17:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 `guest_memfd` 提供直接映射移除支持的补丁系列（[PATCH v6 00/11]）。该补丁旨在通过解除虚拟机客户内存与主机内核直接映射的关联，来防止 Spectre 风格的瞬态执行攻击。

**原始补丁内容**：
补丁系列扩展了 `guest_memfd` 的功能，使其能够从主机内核的直接映射中移除内存。这一措施可以有效阻止通过直接映射进行的投机性读取，从而保护 KVM 客户机的内存。

**历史讨论要点**：
之前的讨论主要集中在补丁的设计和实现细节上，包括如何处理错误、检查能力以及对相关函数的重命名等。补丁的设计没有发生实质性变化，主要是对错误处理和代码注释进行了修正。

**本周新讨论和进展**：
本周的讨论中，参与者对多个补丁进行了审查和确认，包括：
1. **补丁 1**：对 `->free_folio()` 函数进行了参数修改，以便在内存释放时能够识别是否为直接映射移除的内存。
2. **补丁 3**：引入了 `AS_NO_DIRECT_MAP` 标志，用于标识那些不在直接映射中的映射。
3. **补丁 5**：增加了 `GUEST_MEMFD_FLAG_NO_DIRECT_MAP` 标志，以便在创建 `guest_memfd` 时指定是否移除直接映射。
4. **补丁 10 和 11**：扩展了自测用例，确保在直接映射移除的情况下，客户机仍能正确执行内存操作。

参与者对补丁的整体方向表示认可，并提出了一些小的改进建议。整体来看，补丁系列在技术上得到了积极的反馈，推动了对 KVM 的安全性提升。

#### 📝 邮件列表

1. **[09-12 09:17]** [PATCH v6 00/11] Direct Map Removal Support for guest_memfd
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
2. **[09-12 09:17]** [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
3. **[09-12 09:17]** [PATCH v6 02/11] arch: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[09-12 09:17]** [PATCH v6 03/11] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
5. **[09-12 09:17]** [PATCH v6 04/11] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
6. **[09-12 09:17]** [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
7. **[09-12 09:17]** [PATCH v6 06/11] KVM: selftests: load elf via bounce buffer
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
8. **[09-12 09:17]** [PATCH v6 07/11] KVM: selftests: set KVM_MEM_GUEST_MEMFD in
 vm_mem_add() if guest_memfd != -1
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[09-12 09:17]** [PATCH v6 08/11] KVM: selftests: Add guest_memfd based
 vm_mem_backing_src_types
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[09-12 09:17]** [PATCH v6 09/11] KVM: selftests: stuff vm_mem_backing_src_type into
 vm_shape
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
11. **[09-12 09:17]** [PATCH v6 10/11] KVM: selftests: cover GUEST_MEMFD_FLAG_NO_DIRECT_MAP
 in existing selftests
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
12. **[09-12 09:17]** [PATCH v6 11/11] KVM: selftests: Test guest execution from direct map
 removed gmem
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
13. **[09-12 11:48]** Re: [PATCH v6 01/11] filemap: Pass address_space mapping to
 ->free_folio()
   - 发件人: Pedro Falcato <pfalcato@suse.de>
14. **[09-14 10:35]** Re: [PATCH v6 03/11] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Mike Rapoport <rppt@kernel.org>
15. **[09-14 10:44]** Re: [PATCH v6 05/11] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>

---

### Thread 4: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 14:22:47 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构上对非虚拟化（NV）虚拟机的特性限制的补丁系列，标题为“[PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support”。

1. **原始补丁内容**：该补丁系列旨在调整当前对 NV 虚拟机的特性限制，以更好地反映实际支持的状态。补丁包括将特性掩码转换为拒绝列表（denylist），并修复了对某些特性的错误声明（如 FEAT_DoubleLock）。

2. **之前讨论要点**：在之前的讨论中，参与者提到由于 NV 支持尚未合并，特性选择较为灵活。随着 NV 的合并，现有的特性限制逻辑需要更新，以避免未来的 MMU 和 TLB 行为受到限制。

3. **本周新讨论及进展**：本周的讨论主要集中在 Oliver Upton 提出的多个补丁上，逐一修复了对 NV 虚拟机的特性声明，包括暴露 FEAT_DF2、FEAT_RASv1p1、FEAT_ECBHB 等特性。此外，Marc Zyngier 对补丁的逻辑表示认可，并表示将进一步审查该系列补丁。整体来看，讨论强调了更新特性声明的重要性，以确保 KVM 的功能与硬件支持相匹配。

#### 📝 邮件列表

1. **[09-12 14:22]** [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-12 14:22]** [PATCH 01/11] KVM: arm64: nv: Convert masks to denylists in limit_nv_id_reg()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-12 14:22]** [PATCH 02/11] KVM: arm64: nv: Don't erroneously claim FEAT_DoubleLock for NV VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[09-12 14:22]** [PATCH 03/11] KVM: arm64: nv: Expose FEAT_DF2 to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-12 14:22]** [PATCH 04/11] KVM: arm64: nv: Expose FEAT_RASv1p1 via RAS_frac
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-12 14:22]** [PATCH 05/11] KVM: arm64: nv: Expose FEAT_ECBHB to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-12 14:22]** [PATCH 06/11] KVM: arm64: nv: Expose FEAT_AFP to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-12 14:22]** [PATCH 07/11] KVM: arm64: nv: Exclude guest's TWED configuration when TWE isn't set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-12 14:22]** [PATCH 08/11] KVM: arm64: nv: Expose FEAT_TWED to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-12 14:22]** [PATCH 09/11] KVM: arm64: nv: Advertise FEAT_SpecSEI to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-12 14:22]** [PATCH 10/11] KVM: arm64: nv: Advertise FEAT_TIDCP1 to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-12 14:22]** [PATCH 11/11] KVM: arm64: nv: Expose up to FEAT_Debugv8p8 to NV-enabled VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-12 22:43]** Re: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with current state of support
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[09-12 14:48]** Re: [PATCH 00/11] KVM: arm64: nv: Align feature limitations with
 current state of support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 5: [PATCH v16 0/6] KVM: arm64: Provide guest support for GCS

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 10:25:26 +0100

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v16 0/6] KVM: arm64: 提供对 GCS 的客体支持”，主要涉及对 ARM64 架构的 Guarded Control Stack (GCS) 特性的支持。GCS 是一种硬件保护机制，旨在增强对返回导向编程（ROP）攻击的防护，并简化应用程序的调用栈收集。

**原始 patch/问题内容**：
该系列补丁实现了对 KVM 客体的 GCS 管理，允许虚拟机使用 GCS 特性。GCS 通过硬件保护返回地址栈，增强了系统的安全性。

**之前讨论要点**：
在历史讨论中，补丁经历了多次版本迭代，主要集中在如何管理 GCS 的访问和寄存器的上下文切换、异常处理等方面。补丁的设计目标是确保 GCS 的操作在 KVM 环境中能够正确执行，避免潜在的安全隐患。

**本周的新讨论与进展**：
本周的讨论中，Mark Brown 提出了多个补丁，涵盖了 GCS 寄存器的管理、异常处理中的 PSTATE.EXLOCK 设置、以及在 GCS 启用时的寄存器访问验证。Marc Zyngier 对补丁中的一些实现提出了疑问，特别是关于寄存器访问的生命周期管理和异常返回的处理逻辑。讨论中也提到需要更新相关注释和增加测试，以确保代码的正确性和稳定性。

总体来看，本周的讨论推动了 GCS 支持的进一步完善，确保其在 KVM 中的安全性和有效性。

#### 📝 邮件列表

1. **[09-12 10:25]** [PATCH v16 0/6] KVM: arm64: Provide guest support for GCS
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-12 10:25]** [PATCH v16 1/6] arm64/gcs: Ensure FGTs for EL1 GCS instructions
 are disabled
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-12 10:25]** [PATCH v16 2/6] KVM: arm64: Manage GCS access and registers for
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-12 10:25]** [PATCH v16 3/6] KVM: arm64: Set PSTATE.EXLOCK when entering an
 exception
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[09-12 10:25]** [PATCH v16 4/6] KVM: arm64: Validate GCS exception lock when
 emulating ERET
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[09-12 10:25]** [PATCH v16 5/6] KVM: arm64: Allow GCS to be enabled for guests
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[09-12 10:25]** [PATCH v16 6/6] KVM: selftests: arm64: Add GCS registers to
 get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[09-12 12:59]** Re: [PATCH v16 2/6] KVM: arm64: Manage GCS access and registers for guests
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-12 13:06]** Re: [PATCH v16 4/6] KVM: arm64: Validate GCS exception lock when emulating ERET
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-12 17:33]** Re: [PATCH v16 2/6] KVM: arm64: Manage GCS access and registers for
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[09-12 18:14]** Re: [PATCH v16 2/6] KVM: arm64: Manage GCS access and registers for
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[09-12 22:30]** Re: [PATCH v16 2/6] KVM: arm64: Manage GCS access and registers for guests
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[09-12 22:44]** Re: [PATCH v16 5/6] KVM: arm64: Allow GCS to be enabled for guests
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[09-12 22:46]** Re: [PATCH v16 6/6] KVM: selftests: arm64: Add GCS registers to get-reg-list
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 9 Sep 2025 14:46:42 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上捐赠内存的新功能的补丁（PATCH v4 01/28）。该补丁旨在添加一个新的函数，以便在捐赠内存时指定权限（prot）。

在之前的讨论中，参与者们对补丁的实现细节进行了探讨，特别是关于内存权限的处理。Mostafa Saleh 提出了是否应该强制权限为 KVM_PGTABLE_PROT_RW 的建议，以确保内存类型的正确性，而不是仅仅关注权限。Will Deacon 也对补丁的逻辑提出了质疑，认为在检查 pfn（页面框架号）时应确保其确实为 MMIO（内存映射输入输出），并且应检查该 pfn 是否已被 hypervisor 所拥有。

在本周的新讨论中，Will Deacon 对补丁的多个方面进行了深入分析，提出了对现有检查逻辑的改进建议，强调了在捐赠内存时需要确保内存权限的正确性。此外，Pranjal Shrivastava 也支持 Deacon 的观点，认为当前的 WARN_ON 检查可能会导致某些不当的内存捐赠未被捕获。整体来看，本周的讨论集中在如何确保内存捐赠的安全性和有效性上，参与者们对补丁的细节进行了细致的审查和建议。

#### 📝 邮件列表

1. **[09-09 14:46]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-09 15:12]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-09 15:16]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Will Deacon <will@kernel.org>
4. **[09-09 15:23]** Re: [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-09 15:25]** Re: [PATCH v4 07/28] iommu/arm-smmu-v3: Move TLB range invalidation
 into a macro
   - 发件人: Will Deacon <will@kernel.org>
6. **[09-09 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>
7. **[09-09 16:56]** Re: [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-09 11:30]** Re: [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp SMMUv3
   - 发件人: Daniel Mentz <danielmentz@google.com>
9. **[09-12 14:52]** Re: [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Will Deacon <will@kernel.org>
10. **[09-12 14:54]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Will Deacon <will@kernel.org>
11. **[09-12 15:18]** Re: [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Will Deacon <will@kernel.org>
12. **[09-14 19:23]** Re: [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory
 with prot
   - 发件人: Pranjal Shrivastava <praan@google.com>
13. **[09-14 20:41]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Pranjal Shrivastava <praan@google.com>

---

### Thread 7: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  9 Sep 2025 08:24:27 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是在虚拟机初始化过程中保留 pKVM VM 句柄，以解决在非保护模式下创建和销毁虚拟机时出现的错误。

**原始补丁/问题内容**：
补丁系列的核心是修复在虚拟机初始化时 pKVM 句柄的分配时机问题。当前，pKVM 句柄的分配仅在第一次 vCPU 运行时进行，这导致在某些情况下，MMU 通知可能会在句柄尚未创建时触发，从而引发错误。

**之前讨论要点**：
在历史讨论中，开发者们关注到现有的 pKVM 句柄分配机制存在潜在的时序问题，尤其是在虚拟机的生命周期管理中。补丁系列旨在通过重构代码和引入新的超调用接口来解决这些问题，确保在虚拟机初始化的早期阶段就能获得有效的 pKVM 句柄。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，Fuad Tabba 提出了多个补丁，涵盖了重命名、代码重构和逻辑分离等方面。补丁最终将 pKVM 句柄的保留移至 `pkvm_init_host_vm()` 函数中，以确保在虚拟机的初始设置阶段就能获得句柄。Mark Brown 对补丁进行了测试并确认其正常工作，表示支持该补丁的合并。整体而言，此次补丁系列为 pKVM 的稳定性和可维护性做出了重要贡献。

#### 📝 邮件列表

1. **[09-09 08:24]** [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-09 08:24]** [PATCH v4 1/9] KVM: arm64: Add build-time check for duplicate
 DECLARE_REG use
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[09-09 08:24]** [PATCH v4 2/9] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[09-09 08:24]** [PATCH v4 3/9] KVM: arm64: Rename 'host_kvm' to 'kvm' in pKVM host code
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[09-09 08:24]** [PATCH v4 4/9] KVM: arm64: Clarify comments to distinguish pKVM mode
 from protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[09-09 08:24]** [PATCH v4 5/9] KVM: arm64: Decouple hyp VM creation state from its handle
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[09-09 08:24]** [PATCH v4 6/9] KVM: arm64: Separate allocation and insertion of pKVM
 VM table entries
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[09-09 08:24]** [PATCH v4 7/9] KVM: arm64: Consolidate pKVM hypervisor VM
 initialization logic
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[09-09 08:24]** [PATCH v4 8/9] KVM: arm64: Introduce separate hypercalls for pKVM VM
 reservation and initialization
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[09-09 08:24]** [PATCH v4 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[09-09 22:17]** Re: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial
 VM setup
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[09-10 09:42]** Re: [PATCH v4 0/9] KVM: arm64: Reserve pKVM VM handle during initial
 VM setup
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 8: [PATCH v2 0/3] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 9 Sep 2025 11:44:12 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中对 EL2 特性字段进行可写性修改的补丁（PATCH v2 0/3）。该补丁旨在允许用户空间降级 EL2 特性（VH、TWED、HCX），以确保在不同特性支持的主机之间进行虚拟机的实时迁移兼容性。

在历史讨论中，补丁的初步版本（v1）已被提出，主要关注于如何使这些特性字段可写。补丁的更新（v2）增加了对 TWED 和 VH 字段的支持，并添加了相应的测试用例。

在本周的新讨论中，参与者对补丁的具体实现进行了深入探讨。Oliver Upton 提出，尽管允许 HCX 字段可写对迁移有利，但在某些情况下可能会导致不一致的用户空间接口行为，因此建议在 v3 中将 ID_AA64MMFR1_EL1.VH 字段保持为不可写。Jinqian Yang 也同意这一点，并表示将在后续版本中进行调整。此外，Marc Zyngier 关注到 FEAT_HCX 的禁用可能影响到其他依赖特性，建议在设计时考虑这些依赖关系。

总结来看，本周的讨论主要集中在对补丁的细节修改和潜在影响的评估上，参与者们一致认为需要确保补丁的实现不会引入复杂性或不一致性。

#### 📝 邮件列表

1. **[09-09 11:44]** [PATCH v2 0/3] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
2. **[09-09 11:44]** [PATCH v2 1/3] KVM: arm64: Make ID_AA64MMFR1_EL1.HCX writable from userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
3. **[09-09 11:44]** [PATCH v2 2/3] KVM: arm64: Make ID_AA64MMFR1_EL1.TWED writable from userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
4. **[09-09 11:44]** [PATCH v2 3/3] KVM: arm64: Make ID_AA64MMFR1_EL1.VH writable from userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
5. **[09-08 22:32]** Re: [PATCH v2 3/3] KVM: arm64: Make ID_AA64MMFR1_EL1.VH writable
 from userspace
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-09 00:00]** Re: [PATCH v2 0/3] KVM: arm64: make EL2 feature fields writable in
 ID_AA64MMFR1_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-09 00:07]** Re: [PATCH v2 1/3] KVM: arm64: Make ID_AA64MMFR1_EL1.HCX writable
 from userspace
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-09 11:10]** Re: [PATCH v2 1/3] KVM: arm64: Make ID_AA64MMFR1_EL1.HCX writable from userspace
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-09 14:38]** Re: [PATCH v2 1/3] KVM: arm64: Make ID_AA64MMFR1_EL1.HCX writable
 from userspace
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-10 09:42]** Re: [PATCH v2 3/3] KVM: arm64: Make ID_AA64MMFR1_EL1.VH writable from
 userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
11. **[09-10 09:42]** Re: [PATCH v2 0/3] KVM: arm64: make EL2 feature fields writable in
 ID_AA64MMFR1_EL1
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
12. **[09-10 09:57]** Re: [PATCH v2 1/3] KVM: arm64: Make ID_AA64MMFR1_EL1.HCX writable
 from userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>

---

### Thread 9: [PATCH 0/6] KVM ARM64 pre_fault_memory

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 14:46:42 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 的 KVM_PRE_FAULT_MEMORY 功能的补丁系列（共六个补丁），旨在减少执行过程中的 stage-2 故障数量，特别是在内存密集型应用的后复制迁移场景中。补丁的主要内容包括对现有代码的重构、添加预故障标志、实现 KVM_PRE_FAULT_MEMORY ioctl 以及更新自测试用例以支持 ARM64。

在历史讨论中，补丁的背景是 KVM_PRE_FAULT_MEMORY 功能最初仅在 x86 上可用，现计划将其扩展到 ARM64。补丁系列的第一部分是准备性重构，后续补丁则逐步实现预故障功能。

本周的新讨论中，Jack Thomson 提出了补丁的具体实现细节，包括对内存故障处理函数的修改和自测试用例的更新。Oliver Upton 对补丁提出了一些质疑，建议在处理故障时应考虑合成故障上下文，并对重试逻辑的必要性表示疑虑。此外，他指出了文档中关于 PTE 状态的描述不应特定于 x86，建议进行相应的更新。

总体来看，本周讨论集中在补丁的实现细节和潜在的设计改进上，参与者对如何更好地处理故障和文档准确性进行了深入探讨。

#### 📝 邮件列表

1. **[09-11 14:46]** [PATCH 0/6] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[09-11 14:46]** [PATCH 1/6] KVM: arm64: Add __gmem_abort and __user_mem_abort
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[09-11 14:46]** [PATCH 2/6] KVM: arm64: Add KVM_PGTABLE_WALK_PRE_FAULT walk flag
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
4. **[09-11 14:46]** [PATCH 3/6] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
5. **[09-11 14:46]** [PATCH 4/6] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
6. **[09-11 14:46]** [PATCH 5/6] KVM: selftests: Enable pre_fault_memory_test for arm64
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
7. **[09-11 14:46]** [PATCH 6/6] KVM: selftests: Add option for different backing in pre-fault tests
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
8. **[09-11 11:27]** Re: [PATCH 1/6] KVM: arm64: Add __gmem_abort and __user_mem_abort
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-11 11:42]** Re: [PATCH 3/6] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-11 11:56]** Re: [PATCH 0/6] KVM ARM64 pre_fault_memory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH v3 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 27 Aug 2025 11:19:40 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁系列，主要集中在如何在虚拟机初始化过程中保留 pKVM 虚拟机句柄。

**原始补丁/问题内容**：
补丁系列的核心是确保在虚拟机初始化时，能够及时分配 pKVM 句柄，以避免在 MMU 无效化时出现句柄未分配的情况。这一问题在历史邮件中被详细讨论，指出当前的实现存在一个时间窗口，可能导致在虚拟机的内存与主机 MMU 关联之前，句柄尚未创建的情况。

**之前讨论要点**：
历史讨论中提到，补丁 v3 进行了多次修改，包括增加了检查重复 DECLARE_REG 使用的补丁，并且在 Linux 6.17-rc3 上进行了重基。补丁的目标是确保在虚拟机的第一个 vCPU 运行之前，主机能够正确处理 MMU 通知。

**本周的新讨论与进展**：
本周的讨论中，参与者 Mark Brown 报告了在多个 nVHE 平台上，KVM 自测失败的问题，追溯到最近的提交。Fuad Tabba 和 Marc Zyngier 也确认了这一问题，并表示将暂停该系列补丁的合并，直到问题得到解决。Fuad 预计会很快发布修复补丁。整体来看，本周的讨论集中在识别和修复当前实现中的缺陷上，显示出开发者对稳定性的关注。

#### 📝 邮件列表

1. **[08-27 11:19]** [PATCH v3 0/9] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-27 11:19]** [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[09-08 17:05]** Re: [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during
 pkvm_init_host_vm()
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-08 19:43]** Re: [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[09-08 19:52]** Re: [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during
 pkvm_init_host_vm()
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[09-08 19:54]** Re: [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[09-08 19:57]** Re: [PATCH v3 9/9] KVM: arm64: Reserve pKVM handle during pkvm_init_host_vm()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 11: [PATCH v4 0/5] initialize SCTRL2_ELx

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 16:18:16 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于初始化 SCTRL2_ELx 的补丁（PATCH v4 0/5）。该补丁旨在为 ARM64 架构中的 SCTRL2_ELx 寄存器提供初始化支持。

在历史讨论中，Yeoreum Yun 提到他已经对 pKVM、嵌套虚拟化和崩溃路径进行了测试，但 Dave Martin 提出了对补丁的进一步测试需求，尤其是关注 CPU 的挂起/恢复和热插拔功能。他强调，尽管补丁未导致内核崩溃，但并不能完全保证 SCTRL2_ELx 的正确初始化。

本周的新讨论中，Dave Martin 提出需要在文档中补充 FEAT_SCTLR2 的引导要求，并提供了相应的补丁草案。Yeoreum Yun 确认了他使用调试器检查了 SCTLR2_ELx 的设置，并表示会将 Dave 的文档补充内容纳入下一个补丁系列中。他还在继续检查 Dave 的建议，并计划根据反馈重新提交补丁。

总体来看，讨论的重点在于确保 SCTRL2_ELx 的正确初始化和相关文档的完善，参与者之间的沟通顺畅，进展积极。

#### 📝 邮件列表

1. **[09-01 16:18]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
2. **[09-01 19:17]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-03 11:52]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
4. **[09-03 13:08]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-08 12:02]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
6. **[09-08 12:22]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[09-08 13:49]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>

---

### Thread 12: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 27 Aug 2025 17:01:49 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于修复 Hyper-V 驱动中的 NEED_RESCHED_LAZY 问题及使用通用 API 的补丁（PATCH v2 0/7）。该补丁旨在解决 MSHV 根分区及上层 VTL 代码未能正确处理 NEED_RESCHED_LAZY 的错误，并通过将 "kvm" 入口 API 转换为更通用的 "virt" API 来去重 TIF 相关的 MSHV 代码。

在历史讨论中，Sean Christopherson 提出了补丁的初步版本，并说明了其基于 hyperv-next 分支的背景。Wei Liu 在后续邮件中确认他已将大部分补丁应用到 hyperv-next 中，但提到有些内容未能及时处理。

在本周的新讨论中，Wei Liu 确认了之前遗漏的函数已被处理，Sean Christopherson 对此表示感谢。此外，Joel Fernandes 对补丁中的 RCU 部分进行了审查并给予了认可，标志着该补丁在审查过程中取得了积极进展。

总体而言，此次讨论集中在修复和优化 Hyper-V 驱动的代码上，相关补丁已得到部分确认和审查，预计将进一步推动代码的完善。

#### 📝 邮件列表

1. **[08-27 17:01]** [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-27 17:01]** [PATCH v2 5/7] entry: Rename "kvm" entry code assets to "virt" to
 genericize APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[09-04 23:41]** Re: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
4. **[09-04 22:39]** Re: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[09-09 17:20]** Re: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
6. **[09-10 10:45]** Re: [PATCH v2 5/7] entry: Rename "kvm" entry code assets to "virt"
 to genericize APIs
   - 发件人: Joel Fernandes <joelagnelf@nvidia.com>

---

### Thread 13: [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 19:46:19 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在使 EL2 特性字段在 ID_AA64MMFR1_EL1 中可被用户空间写入，从而支持虚拟机的实时迁移。

**原始补丁内容**：
补丁的主要目的是允许用户空间降低 EL2 特性（TWED 和 HCX）的值，以确保在特性支持不同的主机之间进行虚拟机迁移时的兼容性。尽管 VH 是 EL2 特性，但在用户空间中仍然保持为不可写。

**之前讨论要点**：
在之前的讨论中，参与者对补丁的可行性和潜在的用户空间接口（UAPI）行为表示担忧。Marc Zyngier 提出，允许某些字段可写可能会导致混淆，建议将整个寄存器视为保留位（RES0），以简化 KVM 代码。

**本周新讨论与进展**：
本周的讨论中，Jinqian Yang 提出了补丁的更新版本（v3），并对 TWED 和 HCX 字段的可写性进行了调整。Oliver Upton 对补丁表示认可，但仍对 NV（非虚拟化）影响提出疑问。Marc Zyngier 则表示已推送了一个实现该补丁的分支，尽管尚未经过充分测试。这表明补丁正在向前推进，但仍需更多验证以确保其合理性。

#### 📝 邮件列表

1. **[09-11 19:46]** [PATCH v3 0/2] KVM: arm64: make EL2 feature fields writable in ID_AA64MMFR1_EL1
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
2. **[09-11 19:46]** [PATCH v3 1/2] KVM: arm64: Make ID_AA64MMFR1_EL1.{HCX, TWED} writable from userspace
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
3. **[09-11 19:46]** [PATCH v3 2/2] KVM: arm64: selftests: Test writes to ID_AA64MMFR1_EL1.{HCX, TWED}
   - 发件人: Jinqian Yang <yangjinqian1@huawei.com>
4. **[09-12 14:51]** Re: [PATCH v3 1/2] KVM: arm64: Make ID_AA64MMFR1_EL1.{HCX, TWED}
 writable from userspace
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-14 21:27]** Re: [PATCH v3 1/2] KVM: arm64: Make ID_AA64MMFR1_EL1.{HCX, TWED} writable from userspace
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:38:00 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构下 futex 原子操作的重构，具体的补丁为「[PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic operation」。

在历史讨论中，虽然没有具体的邮件内容提供，但可以推测该补丁旨在优化和重构现有的 futex 原子操作，以提高代码的可读性和性能。

在本周的新讨论中，参与者对补丁进行了深入的技术交流。Will Deacon 提出了对将存储操作推迟到某个位置的疑问，Yeoreum Yun 则建议将 oval 参数从 `arch_futex_atomic_op_inuser()` 传递，以增强可读性。Catalin Marinas 对补丁表示认可，并指出了在第六个补丁中可能存在的函数调用顺序问题，最终给予了该补丁「Reviewed-by」的评价。尽管他在后续邮件中对补丁的命名提出了不同看法，最终还是确认了补丁的良好状态。

总体来看，本周的讨论集中在补丁的实现细节和可读性优化上，参与者们对补丁的方向表示支持，并提出了建设性的意见。

#### 📝 邮件列表

1. **[09-11 16:38]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:04]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-12 17:44]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-12 17:53]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[09-12 18:01]** Re: [PATCH RESEND v7 4/6] arm64: futex: refactor futex atomic
 operation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 15: [PATCH v4 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 8 Sep 2025 12:48:52 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中 EL2 设置的基本支持，以便在 EL0/1 中使用 FEAT_{LS64, LS64_V} 特性。原始的 patch（[PATCH v4 4/7]）旨在为这些特性提供必要的基础设施。

在之前的讨论中，参与者们关注了如何安全地在用户空间中使用这些指令，特别是它们对内存类型的要求以及在不支持的内存位置访问时可能引发的数据中止（SIGBUS）。Will Deacon 提出，盲目暴露这些特性可能会导致不良后果，用户空间需要一种机制来探测或请求支持这些指令的内存区域。

本周的新讨论中，Yicong Yang 解释了在访问不支持的内存区域时，系统会如何处理数据中止，并指出用户空间驱动程序可以利用这些特性直接与硬件交互。Will Deacon 继续质疑如何安全地向用户空间暴露这些指令，尤其是在物理位置不支持指令的情况下。Jonathan Cameron 也对此表示关注，询问是否有简单的方法来标识适合的内存区域。

总体来看，本周的讨论集中在如何安全、有效地将新特性引入用户空间，以及如何处理潜在的错误情况。

#### 📝 邮件列表

1. **[09-08 12:48]** Re: [PATCH v4 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-08 13:01]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
3. **[09-09 09:48]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[09-11 16:50]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Will Deacon <will@kernel.org>
5. **[09-12 14:47]** Re: [PATCH v4 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>

---

### Thread 16: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Sun,  7 Sep 2025 17:59:58 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构中 TCR_EL1 寄存器字段宏的清理和更新，主要由 Anshuman Khandual 提出。历史讨论中，Anshuman 提到当前 TCR_EL1 字段宏分散在 ARM64 平台代码中，包括 KVM 实现，计划通过更新寄存器字段定义并进行必要的替换来进行清理。所有相关的 TCR_XXX 宏已从 `asm/pgtable-hwdef.h` 移动到 KVM 头文件 `asm/kvm_arm.h`，以便在 KVM 中继续使用。此清理不会引入功能性变化。

在本周的新讨论中，Mark Brown 对 Anshuman 提出的第二个补丁进行了审核，确认更新的 TCR_EL1 字段与最新的 ARM 文档一致，并表示虽然清理冗余定义可以作为单独的补丁处理，但并不重要。Anshuman 也同意将 SYS_TCR_EL1 定义的删除作为单独补丁的想法。最终，讨论达成共识，认为当前的补丁是合理的。

总结而言，本周讨论主要集中在对补丁的审核和对冗余定义处理的建议上，整体进展顺利。

#### 📝 邮件列表

1. **[09-07 17:59]** [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-07 17:59]** [PATCH V4 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-08 14:58]** Re: [PATCH V4 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-09 09:20]** Re: [PATCH V4 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[09-09 12:22]** Re: [PATCH V4 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 17: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:22:24 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的 futex 支持新指令 FEAT_LSUI 的补丁（patch）。该补丁旨在改进 futex 的实现，以便更好地利用新引入的指令集。

在历史讨论中，参与者们探讨了该补丁的设计意图，认为新指令并非专门为 futex 而设计，而是更适用于原子操作（atomic_op）。补丁的目标是保持现有行为不变，仅移除对 PSTATE 的更改。

本周的新讨论中，Will Deacon 提出了对补丁的疑问，考虑使用比较和交换（CAS）指令是否比现有的独占操作更优。Yeoreum Yun 进一步分析了补丁的实现，指出虽然可以将某些操作替换为 CAS，但这可能会导致行为变化，建议保持现有逻辑。Catalin Marinas 则提出可以简化代码，去掉不必要的分支，并对补丁表示认可。

总体来看，本周的讨论集中在补丁的实现细节及其对现有行为的影响上，参与者们对如何优化 futex 的实现进行了深入的技术交流。

#### 📝 邮件列表

1. **[09-11 16:22]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:45]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-12 18:09]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[09-12 18:16]** Re: [PATCH RESEND v7 6/6] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 18: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Sep 2025 17:27:40 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 Linux 内核的补丁（patch），其内容为“PMCR_EL0.N 是 RAZ/WI。在 Ubuntu 22.04 LTS 中至少出现了构建失败，建议移除设置函数”。该补丁由 Itaru Kitayama 提出，主要是为了修复在旧版 Ubuntu 22.04 LTS 中出现的构建失败问题，认为写入 PMCR_EL0.N 字段是无效的，因此建议删除相关的设置函数。

在之前的讨论中，Marc Zyngier 对补丁的有效性提出质疑，认为补丁的提交信息不够清晰，无法明确指出修复的具体问题。他指出，KVM 允许用户空间写入 PMCR_EL0.N，这一行为不会改变，因此对补丁的必要性表示怀疑。

在本周的新讨论中，Itaru Kitayama 表示如果补丁没有必要，他将放弃该补丁。Marc Zyngier 则强调希望 Itaru 能够提供更多的背景信息，以便进行深入讨论和修复问题，而不是简单地放弃补丁。

总结来看，本周的讨论主要围绕补丁的有效性和必要性展开，尽管 Itaru 提出了补丁，但由于缺乏足够的解释和背景，导致讨论未能达成共识。

#### 📝 邮件列表

1. **[09-12 17:27]** [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu
 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>
2. **[09-12 12:00]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-12 20:33]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Itaru Kitayama <itaru.kitayama@gmail.com>
4. **[09-12 13:11]** Re: [PATCH] PMCR_EL0.N is RAZ/WI. At least a build failes in Ubuntu 22.04 LTS. Remove the set function.
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 29 Aug 2025 10:51:40 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 系统寄存器（sysreg）定义的修复补丁（PATCH v3 0/3）。历史讨论中，Fuad Tabba 提出了 sysreg 定义文件中的几个错误，包括枚举值 NSACR_RFR 的设置不正确（应为 0b0010 而非 0b0001），以及枚举 DoubleLock 和 EIESB 的符号定义错误（应为有符号和无符号）。此外，文件中存在一些冗余定义，如 RCWSMASK_EL1，这些冗余定义虽然不错误，但可能导致未来的代码问题。

在本周的新讨论中，Fuad Tabba 重申了补丁的内容，强调了修复枚举和移除冗余定义的重要性，并提到为 sysreg 头文件生成脚本添加了验证检查，以减少未来错误的发生。随后，Will Deacon 确认已将该补丁应用于 ARM64 的开发分支，并提供了每个补丁的链接。

总结来看，本周的进展是补丁已成功应用，且对 sysreg 定义的修复和验证机制的引入将有助于提高代码的可靠性。

#### 📝 邮件列表

1. **[08-29 10:51]** [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-09 08:23]** [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[09-09 09:49]** Re: [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and
 generation script
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[09-11 17:11]** Re: [PATCH v3 0/3] arm64: sysreg: Fix sysreg field definitions and generation script
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 20: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Sep 2025 16:28:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的 futex 相关的补丁，标题为“[PATCH v7 RESEND 5/6] arm64: futex: small optimisation for __llsc_futex_atomic_set()”。该补丁旨在对 `__llsc_futex_atomic_set()` 函数进行小幅优化，具体是减少一条指令。

在历史讨论中，参与者们对该补丁的必要性和效果进行了初步探讨，但没有详细记录。进入本周的新讨论后，参与者们对补丁的价值提出了质疑。Will Deacon 表示不确定这项优化是否真的有意义，并指出增加新的汇编代码可能会影响可维护性。Yeoreum Yun 也表达了类似的看法，虽然他认为即使是小的优化也有其价值，但如果从可维护性角度来看不佳，则可以考虑放弃这个补丁。Catalin Marinas 最后建议，除非能证明有明显的性能提升，否则建议暂时搁置该补丁。

总体来看，本周的讨论集中在对补丁的实际效益和可维护性之间的权衡上，参与者们倾向于对该补丁持谨慎态度。

#### 📝 邮件列表

1. **[09-11 16:28]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:19]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-12 17:36]** Re: [PATCH v7 RESEND 5/6] arm64: futex: small optimisation for
 __llsc_futex_atomic_set()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 21: [PATCH] KVM: arm64: nv: Exclude guest's TWED configuration when TWE isn't set

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  9 Sep 2025 00:16:02 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 TWED（Trap Watchpoint Exception Descriptor）配置的问题。原始的 patch 提出了在 TWE（Trap Watchpoint Enable）未设置时，排除客体的 TWED 配置，以避免潜在地延迟主机所需的陷阱。

在之前的讨论中，Oliver Upton 提出了这个 patch，指出 KVM 在处理客体的 TWEDEL 和 TWEDEn 值时，可能会在客体禁用 WFE（Wait For Event）陷阱的情况下，错误地将这些值合并到最终的配置中。这样做可能会影响主机的陷阱处理。

本周的新讨论中，Marc Zyngier 对 patch 提出了疑问，认为当前的实现可能会导致 TWED 从功能集中完全移除，因此 HCR_EL2 中的 TWEDEn 和 TWEDEL 应该保持为 0。他询问是否还有其他方式让客体设置这些位。对此，Oliver Upton 解释说，他在看到 Jinqian 的更改后，未检查限制条件，计划在后续版本中放宽这些限制。

总结而言，本周的讨论主要集中在对 patch 的理解和实现细节的澄清上，Oliver Upton 将在后续版本中进行调整。

#### 📝 邮件列表

1. **[09-09 00:16]** [PATCH] KVM: arm64: nv: Exclude guest's TWED configuration when TWE isn't set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-09 10:07]** Re: [PATCH] KVM: arm64: nv: Exclude guest's TWED configuration when TWE isn't set
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-09 14:28]** Re: [PATCH] KVM: arm64: nv: Exclude guest's TWED configuration when
 TWE isn't set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 22: [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Tue,  9 Sep 2025 13:36:29 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 和 nvhe 的内核补丁，主要目的是在系统崩溃时能够转储故障指令，以便于调试内存损坏问题。

**原始补丁内容**：
补丁系列包含两个部分：第一个补丁为 nvhe 添加了在崩溃时转储故障指令的支持；第二个补丁则为 pKVM 提供类似的支持，且在主机的 stage-2 中将 hypervisor 代码映射为只读（RO）。

**之前讨论要点**：
在历史讨论中，参与者探讨了如何在崩溃时有效地获取并转储故障指令。补丁的设计考虑了在崩溃时主机 CPU 没有 stage-2 的情况，因此可以直接重用内核代码来读取和转储指令。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的细节上，Mostafa Saleh 提出了补丁的更新版本（v2），并根据反馈进行了增强，确保指令转储的安全性。此外，补丁已获得 Kunwu Chan 的测试和审核，Will Deacon 也对此表示认可。整体来看，补丁的实现和测试进展顺利，预计将为内核调试提供更好的支持。

#### 📝 邮件列表

1. **[09-09 13:36]** [PATCH v2 0/2] Dump instructions on panic for pKVM/nvhe
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-09 13:36]** [PATCH v2 1/2] KVM: arm64: Dump instruction on hyp panic
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[09-09 13:36]** [PATCH v2 2/2] KVM: arm64: Map hyp text as RO and dump instr on panic
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 23: [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Sun,  7 Sep 2025 13:14:13 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的 vgic（虚拟中断控制器）中修复不正确的自旋锁 API 使用。历史讨论中，Alok Tiwari 提出了一个补丁，指出函数 vgic_flush_lr_state() 错误地调用了低级 API _raw_spin_unlock()，而应该使用更为合适的 raw_spin_unlock()。这个修改旨在避免对内部函数的误用，并确保 vgic 代码中的锁定语义符合内核的约定。

在本周的新讨论中，Marc Zyngier 对补丁进行了反馈，建议删除一些冗余的描述，并确认了补丁的修改意见，表示支持（Acked-by）。Alok Tiwari 随后回应表示将根据 Marc 的建议提交补丁的第二版（v2）。

总体来看，本周的讨论主要集中在对补丁的细节修改和确认支持上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[09-07 13:14]** [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Alok Tiwari <alok.a.tiwari@oracle.com>
2. **[09-08 09:16]** Re: [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-08 18:36]** Re: [External] : Re: [PATCH] KVM: arm64: vgic: fix incorrect spinlock
 API usage
   - 发件人: ALOK TIWARI <alok.a.tiwari@oracle.com>

---

### Thread 24: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Sep 2025 16:09:42 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 FEAT_LSUI 并将其应用于 futex 原子操作的补丁（patch）。该补丁的目的是增强 Linux 内核在处理原子操作时的性能，特别是在 futex 机制中。

在历史讨论中，参与者们对该补丁的必要性和实现细节进行了初步探讨，但具体的技术细节和架构规范（Arm ARM）并未在邮件中详细列出。

在本周的新讨论中，Will Deacon 表达了对 FEAT_LSUI 相关文档的困惑，指出在最新的 Arm ARM 中找不到相关信息，并询问应该查看哪些资料。Catalin Marinas 随后回应，指出目前该信息仅在公共 XML 中可用，预计到年底会有 Arm ARM 的正式发布，或者在私有的 2024 架构规范中找到，但这并不是理想的解决方案。他表示，如果参与者希望等待公共规范的发布，他对此表示理解。

总体来看，本周的讨论主要集中在对 FEAT_LSUI 相关文档的可用性和获取途径的探讨，尚未对补丁本身的实现细节进行深入分析。

#### 📝 邮件列表

1. **[09-11 16:09]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-11 17:22]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 25: [PATCH] KVM: arm64: Fix parameter ordering for VBAR_EL1 assignment

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  8 Sep 2025 17:35:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要涉及 VBAR_EL1（向量基地址寄存器）的参数顺序修复。

**原始补丁内容**：
补丁的核心是修正 `__vcpu_assign_sys_reg()` 函数调用中参数的顺序。该函数期望第二个参数为寄存器 ID，第三个参数为要赋值的内容，而原有代码传递的顺序不正确。修复后，确保在处理异常前，vCPU 的 VBAR_EL1 值与客体的值一致，从而在恢复客体时能够正确处理异常。

**之前的讨论要点**：
在历史讨论中并没有相关的背景信息，所有讨论均集中在本周的新进展上。

**本周的新讨论与进展**：
本周，Fuad Tabba 提出了补丁并详细说明了修复的必要性。随后，Oliver Upton 对此补丁表示感谢，并确认已将其应用于修复分支。这表明该补丁已被接受并将纳入后续的代码版本中。

#### 📝 邮件列表

1. **[09-08 17:35]** [PATCH] KVM: arm64: Fix parameter ordering for VBAR_EL1 assignment
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-08 11:23]** Re: [PATCH] KVM: arm64: Fix parameter ordering for VBAR_EL1 assignment
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 26: [PATCH v2] KVM: arm64: Remove stage 2 read fault check

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  8 Sep 2025 14:48:06 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下移除 stage 2 读取故障检查的补丁（patch）内容。补丁的主要目的是在非 NV（Non-Virtualization）情况下，映射 stage-2 时始终授予读取权限，因此进行读取权限检查没有实际意义。而对于 NV 客户端，shadow stage-2 可能会有非可读的映射，因此在这种情况下也不应进行读取故障检查。

在历史讨论中，补丁的初步版本（v1）已被提出，经过建议者 Oliver Upton 和 Marc Zyngier 的反馈后，补丁在 v2 版本中进行了修改，直接移除了读取故障检查，而不是仅在 NV 情况下跳过该检查。

在本周的新讨论中，Wei-Lin Chang 提交了补丁 v2，并说明了修改的原因和背景。Oliver Upton 随后确认已将该补丁应用于修复列表，表示感谢。这表明该补丁得到了认可并将被纳入后续的代码更新中。

#### 📝 邮件列表

1. **[09-08 14:48]** [PATCH v2] KVM: arm64: Remove stage 2 read fault check
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[09-08 11:23]** Re: [PATCH v2] KVM: arm64: Remove stage 2 read fault check
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 27: [PATCH v2] KVM: arm64: vgic: fix incorrect spinlock API usage

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  8 Sep 2025 11:04:11 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic（虚拟中断控制器）代码中，修复不正确的自旋锁 API 使用问题。

1. **原始 patch/问题的内容**：本次 patch 的目的是修正函数 `vgic_flush_lr_state()` 中错误地调用了低级 API `_raw_spin_unlock()`，而应使用 `raw_spin_unlock()`。后者确保了在 vgic 代码中正确的锁定语义。

2. **之前的讨论要点**：在历史讨论中没有相关的讨论记录，但该 patch 是基于之前的提交（8fa3adb8c6be），该提交将 `vgic_irq->irq_lock` 修改为一个自旋锁。

3. **本周的新讨论、进展或结论**：本周的讨论中，Alok Tiwari 提交了该 patch 的 v2 版本，并在邮件中指出了修复的内容。该 patch 已获得 Marc Zyngier 的认可（Acked-by），并被 Oliver Upton 确认已应用到修复列表中。这标志着修复工作已顺利推进并得到认可。

#### 📝 邮件列表

1. **[09-08 11:04]** [PATCH v2] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Alok Tiwari <alok.a.tiwari@oracle.com>
2. **[09-08 11:23]** Re: [PATCH v2] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 28: [PATCH v11 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A
 initialization and in host handler

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 8 Sep 2025 15:38:58 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下使用 SMCCC 1.2（Secure Monitor Call Convention Call 1.2）进行 FF-A（Firmware Framework for Arm）初始化及主机处理的补丁（patch）。该补丁是 v11 版本的第 2/6 个补丁，旨在改进 KVM 对 FF-A 的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于之前对 FF-A 1.2 支持的整体讨论而提出的，可能涉及到如何在 KVM 中有效实现 FF-A 的功能。

在本周的新讨论中，参与者 Will Deacon 对补丁表示认可，并确认补丁的内容看起来很好，表示如果 Marc 也满意的话，该补丁将会通过 kvmarm 树进行合并。这表明补丁得到了积极的反馈，并且有望在未来的版本中被采纳。整体来看，本周的讨论进展顺利，补丁的接受度较高。

#### 📝 邮件列表

1. **[09-08 15:38]** Re: [PATCH v11 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A
 initialization and in host handler
   - 发件人: Will Deacon <will@kernel.org>
2. **[09-08 15:39]** Re: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 29: [PATCH RESEND v7 2/6] KVM: arm64: expose FEAT_LSUI to guest

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 12 Sep 2025 17:25:33 +0100

#### 🤖 AI 总结

本周讨论的主题是关于一个补丁（patch），其内容为“[PATCH RESEND v7 2/6] KVM: arm64: expose FEAT_LSUI to guest”。该补丁旨在将 FEAT_LSUI 特性暴露给 KVM 虚拟机中的 ARM64 客户端，以增强虚拟化性能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是针对 KVM 在 ARM64 架构下的功能扩展进行的讨论，涉及到如何更好地支持虚拟机的特性。

本周的新讨论中，参与者 Catalin Marinas 对该补丁进行了审查，并表示支持，标记为“Reviewed-by”。这表明补丁得到了认可，可能会在后续的版本中进一步推进。

总体来看，本周的进展是补丁获得了审查者的认可，为其后续合并奠定了基础。

#### 📝 邮件列表

1. **[09-12 17:25]** Re: [PATCH RESEND v7 2/6] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 30: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 12 Sep 2025 17:24:11 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的 Kconfig 配置补丁，具体内容为添加对 LSUI（Load Store Unit Instruction）的支持。该补丁旨在检测工具链对 LSUI 的支持情况。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了增强 ARM64 架构在工具链支持方面的能力，特别是与 LSUI 指令相关的功能。

在本周的新讨论中，参与者 Catalin Marinas 对补丁进行了审查，并提出了一些小建议。他建议改进邮件主题，以更清晰地表达补丁的目的，即检测工具链对 LSUI 的支持。此外，他指出 binutils 2.45 版本已添加对 LSUI 的支持，并提到在帮助信息中应使用两个空格的缩进。总体而言，Catalin 对补丁表示认可，并给予了“已审查通过”的意见。

总结来看，该补丁的提出和讨论旨在提升 ARM64 架构的工具链支持，经过审查后得到了积极反馈。

#### 📝 邮件列表

1. **[09-12 17:24]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 31: [PATCH RESEND v7 1/6] arm64: cpufeature: add FEAT_LSUI

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 12 Sep 2025 17:12:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的 CPU 特性补丁，具体内容为添加对 FEAT_LSUI 特性的支持。

在历史讨论中，未提供具体的背景信息，因此我们无法得知该补丁的详细内容或之前的讨论要点。

在本周的新讨论中，参与者 Catalin Marinas 对补丁进行了审阅，并提出了一些修改建议。他指出邮件中有两段内容表达相似，建议将第二段简化为“添加对 FEAT_LSUI 的 CPU 特性检测”，并认为没有必要再次解释 PSTATE.PAN 的内容。最终，他表示对该补丁的审核通过（Reviewed-by）。

总体来看，本周的讨论主要集中在补丁内容的简化和明确性上，未涉及其他新的技术争议或问题。

#### 📝 邮件列表

1. **[09-12 17:12]** Re: [PATCH RESEND v7 1/6] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 32: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 08 Sep 2025 19:42:57 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception”，主要讨论了在进入异常时设置 PSTATE.EXLOCK 的补丁。

在历史讨论中，没有提供具体的背景信息或之前的讨论内容，因此我们无法了解该补丁的详细背景或之前的争论。

本周的新讨论中，Marc Zyngier 对补丁进行了简要回复，指出在 ARM 架构参考手册中可以去掉章节编号，因为这些编号在文档的不同版本中是稳定的。此外，他提到目前只有 NV 的情况需要模拟 ERET，这可能是对补丁实现的一个重要考虑。

总体来看，本周的讨论主要集中在补丁的细节和文档规范上，尚未有进一步的技术进展或结论。

#### 📝 邮件列表

1. **[09-08 19:42]** Re: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 33: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside
 other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 8 Sep 2025 15:19:00 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁（patch），其内容为「[PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes」。该补丁的目的是在进行页面表转储时，不再与其他属性一起测试 PTE_VALID，从而简化处理逻辑。

在历史讨论中，未提供具体的背景信息或之前的讨论内容，因此无法总结出相关的历史要点。

在本周的新讨论中，参与者 Will Deacon 对该补丁表示认可（Acked-by），并假设 Oliver 或 Marc 将通过 kvmarm 树来处理这个补丁。这表明补丁得到了积极的反馈，并可能会在后续的开发中被采纳。

总体来看，本周的讨论主要集中在对补丁的认可和后续处理的预期上，未涉及更深层次的技术细节或争议。

#### 📝 邮件列表

1. **[09-08 15:19]** Re: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside
 other attributes
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 34: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 8 Sep 2025 14:25:18 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 嵌套虚拟化支持的补丁（patch），该补丁的编号为 kvmtool v3 0/6。邮件中提到的补丁旨在增强 KVM 工具对 ARM64 架构的嵌套虚拟化功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了回应之前对 ARM64 嵌套虚拟化的需求和改进建议。参与者 Andre Przywara 提到希望对补丁进行重新整理，以解决 Alexandru 提出的未解决评论，这表明在补丁的开发过程中，存在一些尚需讨论和完善的技术细节。

在本周的新讨论中，Will Deacon 向 Andre 询问是否计划根据 Alexandru 的评论对补丁进行重新修改。这表明该补丁仍在进一步审查和完善的阶段，参与者们关注如何更好地解决之前提出的问题，以推动嵌套虚拟化支持的实现。整体来看，讨论仍在进行中，尚未达成最终结论。

#### 📝 邮件列表

1. **[09-08 14:25]** Re: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Will Deacon <will@kernel.org>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report

**📧 邮件数**: 6 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 10 Sep 2025 08:47:43 +0300

#### 🤖 AI 总结

本邮件讨论围绕一个名为“[RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range found in the interface report”的补丁展开，主要目的是验证MMIO（内存映射输入输出）范围的有效性。补丁提出了在处理设备接口报告时，如何正确识别和验证MMIO地址范围的问题。

在历史讨论中，参与者们探讨了补丁的初步建议和潜在问题，尤其是关于MSI-X表、PBA（中断控制器）和非TEE（可信执行环境）区域的复杂性。讨论指出，如果一个BAR（基址寄存器）包含多个不同的地址范围，可能导致验证失败，因为RSI_VDEV_VALIDATE_MAPPING需要的地址基址不一致。

本周的新讨论中，Arto Merilainen指出，当前的验证机制存在缺陷，建议应能处理与接口报告相同格式的数据。Jason Gunthorpe强调，内核应确保驱动程序不会被误导以映射不安全的MMIO区域。Aneesh Kumar K.V提到，可能需要在接口报告中假设MSI-X表和PBA范围缺失，并建议从配置空间获取相关地址信息。其他参与者也提出了对验证机制的改进建议，包括添加新的TSM操作以支持BAR范围的验证。

总体来看，参与者们一致认为需要建立更健全的验证机制，以确保设备驱动程序能够正确处理MMIO地址，并避免安全隐患。

#### 📝 邮件列表

1. **[09-10 08:47]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
2. **[09-10 11:21]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
3. **[09-11 11:03]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
4. **[09-11 18:31]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
5. **[09-11 10:41]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
6. **[09-11 10:47]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: dan.j.williams <dan.j.williams@intel.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 25 Aug 2025 14:08:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM 架构下的一个锁定错误，具体涉及 `vgic_put_irq` 函数。历史讨论中，syzbot 报告了一个锁定问题，指出在特定的内核提交（7b8346bd9fce）中存在此问题，并提供了相关的控制台输出和构建配置链接。

在之前的讨论中，参与者们关注了该问题的根源以及可能的修复方案。syzbot 提出了一个测试请求，旨在验证修复效果。

在本周的新讨论中，Oliver Upton 回复了 syzbot 的测试请求，表示希望进行进一步的测试。然而，syzbot 报告了测试失败，原因是无法将二进制文件复制到虚拟机，出现了连接超时的问题。这表明当前的修复方案尚未成功应用，且需要进一步的调试和修复工作。

总的来说，尽管有尝试修复该锁定问题，但目前的进展并不理想，后续仍需继续跟进和解决。

#### 📝 邮件列表

1. **[08-25 14:08]** [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq
   - 发件人: syzbot <syzbot+cef594105ac7e60c6d93@syzkaller.appspotmail.com>
2. **[09-09 14:23]** Re: [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-09 15:14]** Re: [syzbot] [kvmarm?] [kvm?] WARNING: locking bug in vgic_put_irq
   - 发件人: syzbot <syzbot+cef594105ac7e60c6d93@syzkaller.appspotmail.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 changes for 6.17, round #3

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 10 Sep 2025 13:25:08 -0700

#### 🤖 AI 总结

本邮件讨论了 KVM/arm64 在 6.17 版本中的最新修复和改动，主要由 Oliver Upton 提出。

1. **原始 patch/问题的内容**：本次讨论的 patch 是 KVM/arm64 的修复集，旨在解决与嵌套虚拟化和虚拟通用中断控制器（VGIC）相关的问题。特别提到了一些与 RCU（读-复制-更新）停滞相关的修复被撤回，因为这些修复中存在引用计数和使用后释放（UAF）问题。

2. **之前的讨论要点**：虽然本次邮件没有提供历史讨论的具体内容，但提到了一些之前的修复未能有效解决问题，因此需要进行撤回和重新评估。

3. **本周的新讨论、进展或结论**：本周的讨论集中在一系列修复上，包括修复 TLB（翻译后备缓冲区）匹配过程、VGIC 的锁顺序问题、以及对 VBAR_EL1 参数排序的修正。此外，Oliver Upton 强调了撤回之前的两个修复，并请求将这些更改合并到主线代码中。

总体而言，本周的讨论展示了对 KVM/arm64 代码的持续关注和改进，特别是在处理复杂的虚拟化场景时。

#### 📝 邮件列表

1. **[09-10 13:25]** [GIT PULL] KVM/arm64 changes for 6.17, round #3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Other

共 3 个 thread

---

### Thread 1: [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  5 Sep 2025 13:41:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的 MTE（Memory Tagging Extension）相关的补丁，旨在修复 MTE granule mask 的生成问题。原始补丁由 Vladimir Murzin 提出，主要修改了 MTE_GRANULE_MASK 的定义，以确保在与 MTE_TAG_SHIFT 一起使用时生成正确的掩码。

在历史讨论中，Vladimir 解释了补丁的具体内容，指出原先的 MTE_GRANULE_MASK 定义存在问题，导致生成的掩码不符合预期。通过修正后，掩码的低位四个比特将被正确设置，从而能够正确屏蔽逻辑标签。

在本周的新讨论中，参与者 Alexandru Elisei 对补丁进行了审查，确认了修正后的掩码生成逻辑是正确的，并询问了如何发现这一问题。Vladimir 回应称，之前的测试未能捕捉到错误，但通过目测检查发现了问题。最后，Andrew Jones 表示已将补丁合并，确认了该修复的有效性。

整体来看，本次讨论围绕补丁的逻辑修正展开，参与者们积极交流，确保了补丁的准确性和有效性。

#### 📝 邮件列表

1. **[09-05 13:41]** [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
2. **[09-08 12:49]** Re: [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[09-08 13:09]** Re: [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
4. **[09-08 13:38]** Re: [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: [syzbot] [kvmarm?] KASAN: invalid-access Read in __kvm_pgtable_walk

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 09 Sep 2025 14:11:30 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KASAN（Kernel Address Sanitizer）在 `__kvm_pgtable_walk` 函数中检测到的无效内存访问问题。该问题由 syzbot 报告，涉及 ARM64 架构的 KVM（Kernel-based Virtual Machine）模块。

在历史讨论中，未提供具体的补丁或背景信息。本周的新讨论中，syzbot 提供了详细的错误报告，包括错误发生的代码位置、调用栈以及相关的内存状态。报告显示，内存访问错误发生在 `__kvm_pgtable_walk` 和 `__kvm_pgtable_visit` 函数中，指向了一个无效的物理地址。

Oliver Upton 在本周的讨论中回复了 syzbot，提出了一个测试命令以验证修复效果。然而，syzbot 随后报告称，尽管应用了相关补丁，但问题依然存在，仍然触发 KASAN 的无效访问错误。

综上所述，目前尚未找到有效的解决方案来修复此 KASAN 报告的问题，后续需要进一步的调试和修复工作。

#### 📝 邮件列表

1. **[09-09 14:11]** [syzbot] [kvmarm?] KASAN: invalid-access Read in __kvm_pgtable_walk
   - 发件人: syzbot <syzbot+31156cb24a340d8e2c05@syzkaller.appspotmail.com>
2. **[09-09 14:22]** Re: [syzbot] [kvmarm?] KASAN: invalid-access Read in
 __kvm_pgtable_walk
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-09 14:52]** Re: [syzbot] [kvmarm?] KASAN: invalid-access Read in __kvm_pgtable_walk
   - 发件人: syzbot <syzbot+31156cb24a340d8e2c05@syzkaller.appspotmail.com>

---

### Thread 3: [syzbot] [kvmarm?] kernel panic: Unhandled exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 09 Sep 2025 10:52:28 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM ARM 虚拟化环境中出现的内核崩溃问题。具体问题是 syzbot 发现了一种未处理异常导致的内核崩溃，相关信息显示在邮件中，包括崩溃时的调用栈和硬件信息。

在历史讨论部分没有相关的背景信息，因此本周的新讨论成为焦点。syzbot 提供了详细的崩溃报告，包括 HEAD 提交信息、内核配置、用户空间架构等。崩溃的具体信息显示在控制台输出中，内核在处理 KVM 虚拟机创建时发生了 panic，提示存在未处理的异常。

本周的讨论主要集中在如何修复这个问题。syzbot 建议如果有人解决了该问题，请在提交的补丁中添加特定的标签以便追踪。邮件中还包含了 reproducer 链接，供开发者测试和重现该问题。

总的来说，本周的讨论强调了 KVM ARM 环境中的内核崩溃问题，并呼吁开发者关注并修复此问题。

#### 📝 邮件列表

1. **[09-09 10:52]** [syzbot] [kvmarm?] kernel panic: Unhandled exception
   - 发件人: syzbot <syzbot+d173b3985bd6b9487fa1@syzkaller.appspotmail.com>

---

