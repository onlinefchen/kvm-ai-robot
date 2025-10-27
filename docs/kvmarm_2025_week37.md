# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:22:46

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

本邮件讨论的主题是关于引入环形缓冲区远程功能的补丁（PATCH v6 02/24）。该补丁旨在增强 Linux 内核中的环形缓冲区，以支持远程访问。

在历史讨论中，补丁的背景和目的得到了阐述，但具体的技术细节并未详细记录。本周的新讨论主要集中在补丁的实现细节和代码审查上。

本周的讨论中，参与者们对补丁的命名、代码结构和注释提出了多项建议。例如，Steven Rostedt 指出，如果某个函数涉及内存分配，名称中应包含“alloc”字样。此外，他还提出了关于代码行长度、魔法数字的使用以及缺乏注释的问题，强调了代码可读性和维护性的重要性。Vincent Donnefort 也积极回应了这些建议，并表示将添加必要的注释和文档，以确保代码的清晰性。

总体而言，本周的讨论推动了补丁的进一步完善，参与者们就如何提高代码质量达成了一致，强调了在实现新功能时保持良好代码习惯的重要性。

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

本邮件线程讨论了两个主要的补丁和相关的技术问题。

首先，补丁 [PATCH 2/2] 提出了将 KVM 的 hyp 代码映射为只读（RO），并在系统崩溃时转储指令的建议。该补丁得到了 Will Deacon 的认可，表示支持这一改动。

在历史讨论中，Mostafa Saleh 提出了对另一个补丁 [PATCH 1/2] 的担忧，认为该函数可能被用于从用户空间转储指令。他建议保持函数名称不变，并在函数内部增加对用户模式和指令指针的检查。Will Deacon 同意了这个建议，并表示会进行相应的修改。

本周的新讨论中，Oliver Upton 提出了两个补丁的回退，理由是在处理阶段2页表时引入了多个错误，且修复未能解决问题。他认为回退是当前最佳选择，以便在新修复版本准备好之前，保持系统稳定。最终，这两个回退补丁得到了应用。

此外，Sebastian Ott 提出了关于添加 KVM PSCI 版本的 VCPU 属性的补丁，目的是支持在不同主机内核版本之间的迁移。讨论中提到，指定特定的 PSCI 版本可以避免因版本不匹配导致的迁移失败。Peter Maydell 对此提出了疑问，要求进一步阐明使用场景。Sebastian 解释了这一需求，强调了在不同主机内核版本间迁移的必要性。

总体来看，本周的讨论集中在补丁的认可、回退和新特性的提出上，反映了对 KVM 和 ARM 架构的持续关注和改进。

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

本邮件线程讨论了一个针对 Linux 内核的补丁系列，主题为“支持从直接映射中移除 guest_memfd”。该补丁系列的主要目的是通过取消虚拟机来宾内存在主机内核的直接映射，以减轻类似 Spectre 的瞬态执行问题。

**原始补丁/问题内容**：
补丁系列的核心是扩展 guest_memfd 的功能，使其能够从主机内核的直接映射中移除内存，从而为在 guest_memfd 中运行的 KVM 来宾提供保护。

**之前讨论要点**：
历史讨论中提到，直接映射的移除可以有效防止通过直接映射进行的投机性读取，进而阻止 Spectre 攻击。补丁系列在设计上没有重大变化，主要集中在错误处理和代码清理等方面。

**本周新讨论、进展或结论**：
本周的讨论主要围绕补丁的具体实现和自测功能展开。补丁中引入了新的标志 GUEST_MEMFD_FLAG_NO_DIRECT_MAP，允许在创建 guest_memfd 时指定移除直接映射。此外，补丁还增加了相关的自测，以确保在直接映射被移除的情况下，来宾仍能正常访问内存。参与者对补丁进行了审查并给予了认可，表明该补丁系列在设计和实现上得到了积极反馈。

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

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的特性限制调整，主要涉及到对 NV（非虚拟化）虚拟机的支持。Oliver Upton 提出了一个补丁系列（共11个补丁），旨在将当前的特性限制与实际支持状态对齐。

在历史讨论中，之前的补丁和讨论主要集中在如何处理 NV VMs 的特性掩码，确保不支持的特性不会被错误地报告为可用。Upton 指出，当前有些特性被隐藏，实际上是可以支持的，且他提出了将特性掩码反转为拒绝列表的建议，以更清晰地表达哪些特性不被支持。

本周的新讨论中，Upton 逐一介绍了每个补丁的内容，包括修复错误的特性声明、暴露新的特性（如 FEAT_DF2、FEAT_RASv1p1、FEAT_ECBHB 等），并对特性限制进行了详细的说明。此外，Marc Zyngier 对补丁的逻辑和未来的 MMU/TLB 行为提出了看法，表示需要重新审视这些限制。

总体来看，本周的讨论进一步推动了对 NV VMs 特性支持的优化，确保 KVM 的功能与硬件能力相匹配。

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

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持受保护的控制栈（Guarded Control Stack, GCS）的补丁系列（PATCH v16 0/6）。GCS 旨在增强对返回导向编程（ROP）攻击的防护，并简化调用栈的收集。补丁实现了对 KVM 客户端的 GCS 管理支持。

在历史讨论中，补丁经历了多个版本的迭代，主要集中在 GCS 的实现细节、异常处理以及与 KVM 的集成。补丁的关键改动包括支持嵌套客户机的 GCS、异常处理中的 PSTATE.EXLOCK 管理、以及 GCS 指令的上下文切换。

本周的新讨论中，Mark Brown 提出了六个补丁，涵盖了 GCS 的注册管理、异常处理、以及允许客户机启用 GCS 的功能。Marc Zyngier 对补丁提出了一些技术反馈，指出在某些情况下，寄存器访问的实现存在问题，并建议更新相关文档以反映最新的实现状态。此外，讨论中提到需要增加测试用例，以确保异常路径的正确性。

总体而言，讨论集中在确保 GCS 功能的正确实现及其与 KVM 的兼容性上，强调了代码的健壮性和测试的重要性。

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

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上新增的补丁，主题为“添加一个捐赠内存的函数”。该补丁的主要目的是允许在内存捐赠时指定权限（prot）。

在历史讨论中，补丁的背景和动机并未详细阐述，但可以推测其目的是为了优化内存管理和权限控制。参与者们在之前的讨论中对补丁的实现细节提出了一些疑问和建议，主要集中在如何确保内存捐赠的权限设置合理，以及在特定情况下如何处理 MMIO（内存映射输入输出）区域的捐赠。

在本周的新讨论中，参与者 Will Deacon 提出了对补丁中权限检查的改进建议，认为应当强制检查权限为 KVM_PGTABLE_PROT_RW，以避免不当的权限设置。此外，针对 MMIO 的捐赠，Deacon 还提到需要先确认页面是否为 MMIO，并且确保该页面未被其他映射占用。其他参与者如 Pranjal Shrivastava 也支持这一观点，并指出当前的检查可能导致某些不当的捐赠行为未被捕获。

总体来看，本周的讨论集中在补丁的权限控制和内存管理的细节上，参与者们积极提出建议以确保补丁的正确性和有效性。

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

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）在arm64架构下的补丁系列，主要目的是在初始虚拟机设置期间保留pKVM虚拟机句柄。补丁系列共包含9个补丁，主要分为两个部分：重构和功能实现。

在历史讨论中，补丁的背景是当前pKVM句柄的分配仅在虚拟机的第一个vCPU运行时进行，这导致在某些情况下可能会出现MMU无效化通知时没有有效句柄的问题。为了解决这个问题，补丁将句柄的创建提前到虚拟机在主机上初始化时进行。

本周的新讨论中，Fuad Tabba详细介绍了补丁的具体内容，包括：
1. 通过重构代码来清晰化变量命名和注释，以减少混淆。
2. 引入新的超调用接口，将虚拟机的保留和初始化过程分开，以便更灵活地管理虚拟机的生命周期。
3. 通过测试验证了补丁的有效性，Mark Brown确认新版本在测试中表现良好。

最终，这些补丁的实施将确保在虚拟机创建的早期阶段就能获得有效的pKVM句柄，从而提高系统的稳定性和可靠性。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在使 EL2 特性字段在 ID_AA64MMFR1_EL1 中可由用户空间写入，以确保虚拟机在不同特性支持的主机之间的实时迁移兼容性。

在历史讨论中，补丁的初稿（v1）已于之前提交，主要内容是允许用户空间降级 EL2 特性（VH、TWED、HCX）。补丁的更新（v2）增加了对 TWED 和 VH 字段的支持，并添加了相应的测试用例。

本周的新讨论中，参与者对补丁的各个部分进行了详细审议。Oliver Upton 提出了对 VH 字段的担忧，认为在暴露 FEAT_VHE 时，vEL2 始终处于 VHE 上下文，因此不应允许其可写。对于 HCX 字段，尽管有利于虚拟机在不同特性支持的主机间迁移，但也存在潜在的兼容性问题。最终，Jinqian Yang 决定在下一个版本（v3）中将 ID_AA64MMFR1_EL1.VH 字段保持为不可写，以简化用户空间的行为和维护 KVM 代码的简洁性。

总结而言，本周的讨论集中在对补丁的细节审查和潜在问题的识别上，确保了补丁在功能性和兼容性方面的平衡。

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

本邮件线程讨论了一个针对 KVM ARM64 的补丁系列，旨在实现 KVM_PRE_FAULT_MEMORY 功能，之前该功能仅在 x86 上可用。该补丁系列包含六个补丁，主要目的是减少执行过程中的 stage-2 故障，特别是在内存密集型应用的后复制迁移场景中。

历史讨论中，补丁的背景是 KVM_PRE_FAULT_MEMORY 功能的引入，旨在优化内存预填充过程，减少因 stage-2 故障导致的延迟。补丁的具体内容包括对现有代码的重构、添加预故障标志、实现 ioctl 支持、修复自测中的未对齐 mmap 分配问题等。

在本周的新讨论中，Jack Thomson 提交了补丁并逐一介绍了每个补丁的功能。Oliver Upton 对补丁提出了几点建议，包括对 EAGAIN 处理的看法，认为应该将其视为合成的 stage-2 中止，并建议在处理逻辑中创建合成故障上下文。此外，他还指出 UAPI 文档中关于 PTE 状态的描述应更明确，以避免误解。

总体而言，本周的讨论集中在补丁的实现细节及其潜在影响上，参与者们对补丁的方向表示支持，但也提出了改进建议。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“在初始虚拟机设置期间保留 pKVM 虚拟机句柄”。该补丁的目的是在虚拟机初始化时提前分配 pKVM 句柄，以避免在虚拟机内存与主机 MMU 关联时出现的潜在问题。

在历史讨论中，Fuad Tabba 提到，当前的实现中，pKVM 句柄仅在第一次运行 vCPU 时分配，这导致在某些情况下可能会出现 MMU 失效的窗口。为了解决这个问题，补丁建议在 `pkvm_init_host_vm()` 函数中提前保留 pKVM 句柄。

在本周的新讨论中，Mark Brown 报告了在多个 nVHE 平台上运行 KVM 自测时出现的失败，指出该问题与最近的提交有关。Fuad 和 Mark 确认了这个问题，并表示将很快提供修复。Marc Zyngier 也表示，在问题明确之前，将暂停该补丁系列的合并。

总结来说，当前的补丁旨在改善 pKVM 句柄的管理，但在实际应用中出现了问题，开发者们正在积极寻找解决方案。

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

本邮件线程讨论的主题是关于初始化 SCTRL2_ELx 的补丁（PATCH v4 0/5）。该补丁旨在为 ARM64 架构的内核提供对 SCTRL2_ELx 寄存器的初始化支持。

在历史讨论中，参与者 Yeoreum Yun 提到他已对 pKVM、嵌套虚拟化及崩溃路径进行了测试，确保补丁不会导致内核崩溃。然而，Dave Martin 提出，虽然补丁未破坏内核，但仍需确保 SCTRL2_ELx 的初始化、保存和恢复等功能在实际使用中是正确的。Yeoreum 进一步确认他使用调试器验证了 SCTRL2_ELx 的设置。

在本周的新讨论中，Dave Martin 提出了一个补丁，旨在文档化 FEAT_SCTLR2 的引导要求，以确保在内核启动时满足特定条件。Yeoreum 对此表示认可，并表示将把这些文档更新纳入下一个补丁系列中。此外，Yeoreum 还确认了他对 CPU 空闲状态和热插拔的测试结果，表示所有检查均符合预期。

总体来看，本周的讨论主要集中在补丁的文档化和测试验证上，参与者们对补丁的进一步完善和测试结果表示积极的反馈。

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

本邮件线程讨论了一个关于 Hyper-V 驱动程序的补丁系列，主要目的是修复 MSHV 根分区和上层 VTL 代码未能正确处理 NEED_RESCHED_LAZY 的问题，并将与 TIF 相关的 MSHV 代码去重，将 "kvm" 入口 API 转换为更通用的 "virt" API。

在历史讨论中，Sean Christopherson 提出了补丁的初步版本，并解释了其背景和目的。Wei Liu 在后续邮件中提到已将大部分补丁应用到 hyperv-next 分支，但有些内容（如 mshv_vtl 的更改）被剔除。Sean 还提到需要将某些函数的删除合并到补丁中，以确保代码整洁。

在本周的新讨论中，Wei Liu 确认了补丁的完成，并感谢了之前的反馈。Joel Fernandes 对补丁中的 RCU 部分进行了审核，并表示支持，标记为“已审核通过”。

总体来看，本周的讨论主要集中在补丁的确认和审核上，表明该补丁系列正在向最终提交迈进。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要涉及将 EL2 特性字段（HCX 和 TWED）设置为可由用户空间写入，以确保在具有不同特性支持的主机之间进行虚拟机的实时迁移时的兼容性。

**原始补丁内容**：
补丁的目标是允许用户空间降低 ID_AA64MMFR1_EL1 中的 HCX 和 TWED 字段的值，从而确保虚拟机在不同主机间迁移时不会因为特性不一致而出现问题。

**之前讨论要点**：
在之前的讨论中，参与者对将某些字段设置为可写的想法表示担忧，认为这可能导致用户空间接口（UAPI）行为混乱。Marc Zyngier 提出了将整个寄存器视为 RES0 的建议，以简化 KVM 代码，并强调用户空间应对特性依赖性保持一定的理智。

**本周新讨论与进展**：
本周的讨论中，Jinqian Yang 提交了补丁的第三版，保持 VH 字段为非可写，并分离了内核补丁和自测补丁。Oliver Upton 对补丁表示认可，但仍对某些非嵌套的 NV（非虚拟化）影响表示关切。Marc Zyngier 则表示已推送了一个实现该补丁的分支，尽管尚未经过充分测试。整体来看，讨论中对补丁的方向达成了一定的共识，但仍需进一步验证其合理性。

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

本邮件讨论的主题是关于对 ARM64 架构下 futex 原子操作的重构补丁（PATCH RESEND v7 4/6）。该补丁旨在优化和重构 futex 的原子操作，以提高代码的可读性和性能。

在之前的讨论中，参与者对补丁的设计和实现进行了初步评估，主要关注如何更好地传递参数以提高代码的可读性。Yeoreum Yun 提出将参数 oval 从 `arch_futex_atomic_op_inuser()` 传递的建议，认为这样做会使代码更易于理解。

在本周的新讨论中，Will Deacon 对补丁的某个设计选择提出了疑问，询问为何将存储操作推迟到特定位置。Yeoreum Yun 对此进行了回应，强调了 inline 函数的使用，并再次提出了参数传递的建议。Catalin Marinas 对补丁表示认可，并指出在后续的补丁中可能需要调整一些函数的调用顺序。他还提到，可能不需要更改某些函数的名称，尤其是在后续补丁中涉及到的操作可能会改变。

总体来看，本周的讨论集中在补丁的细节和参数传递的可读性上，参与者们对补丁的整体方向表示支持，并提出了一些建设性的建议。

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

本邮件讨论的主题是关于 ARM64 架构中 EL2 的基本设置，以支持 FEAT_{LS64, LS64_V} 特性在 EL0/1 的使用。原始的 patch（[PATCH v4 4/7]）旨在为这些特性提供必要的基础设施。

在之前的讨论中，参与者探讨了如何安全地将这些新指令暴露给用户空间。Will Deacon 提出，直接暴露这些特性可能会导致不安全的情况，因为这些指令仅在特定的内存位置有效，且在不支持的内存区域访问时会产生数据异常（SIGBUS）。他强调，用户空间需要一种机制来探测或请求支持这些指令的内存。

本周的新讨论中，Yicong Yang 提供了对 Will Deacon 的担忧的回应，指出在访问不支持的内存区域时，系统会通过 SIGBUS 处理异常，并提到用户空间驱动程序可以利用这些指令与设备直接交互。Will Deacon 进一步询问如何更好地向用户空间暴露适用的内存区域，Jonathan Cameron 也对此表示关注，提出了对解决方案的思考。

总体而言，本周的讨论集中在如何安全有效地将新特性引入用户空间，以及如何处理可能出现的异常情况。

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

本邮件线程讨论了针对 ARM64 架构的 TCR_EL1 寄存器字段宏的清理工作。Anshuman Khandual 提出了两个补丁（PATCH V4 0/2），旨在将分散在 ARM64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏集中到 KVM 头文件中，并更新寄存器字段定义，以符合最新的 ARM 文档 DDI 0487 L.B。这一清理工作不会引入功能上的变化。

在历史讨论中，Khandual 强调了将冗余的 SYS_TCR_EL1 定义从 sysreg.h 中删除的必要性，并表示该补丁适用于 v6.17-rc4 版本。

在本周的新讨论中，Mark Brown 对补丁进行了审查，并表示虽然将冗余定义的清理放在单独的补丁中可能更合适，但这并不重要。Khandual 也同意这一观点，并确认将 SYS_TCR_EL1 定义的删除作为单独补丁的想法。整体来看，本周的讨论主要集中在补丁的审查和对代码清理的进一步确认上。

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

本邮件线程讨论的主题是关于一个补丁（patch），其内容为“arm64: futex: support futex with FEAT_LSUI”。该补丁旨在为 ARM64 架构的 futex 实现支持新的指令集特性 FEAT_LSUI。

在之前的讨论中，参与者们探讨了这个补丁的设计初衷，认为其主要是为了支持原子操作，而不仅仅是为了 futex 的实现。讨论中提到，使用 CAS（比较并交换）指令可能会比当前的实现更有效，但也可能带来复杂性，尤其是在处理 64 位值时。

本周的新讨论中，Will Deacon 和 Yeoreum Yun 对补丁的实现细节进行了深入分析。Yeoreum Yun 提出了补丁可能需要保留与旧值比较的逻辑，以确保行为的一致性。Catalin Marinas 则建议可以去掉某些不必要的函数调用，并认为补丁的实现是合理的，给予了“Reviewed-by”的认可。此外，Will Deacon 认为在某些情况下，可能需要共享部分代码，但考虑到复杂性，最终决定不采用这种方式。

总体来看，本周的讨论集中在补丁的实现细节和潜在的优化上，参与者们对补丁的方向表示支持，但也提出了需要进一步考虑的技术细节。

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

本邮件讨论的主题是关于一个针对 Linux 内核的补丁，内容涉及 PMCR_EL0.N 寄存器的设置函数。补丁的提出者 Itaru Kitayama 指出，在 Ubuntu 22.04 LTS 上构建时出现了失败，原因是对该寄存器的写入操作被标记为 RAZ/WI（Read As Zero / Write Ignored），因此建议删除相关的设置函数。

在之前的讨论中，Marc Zyngier 对补丁的提交信息表示质疑，认为其不够清晰，未能明确指出修复的具体问题（是构建失败还是语义缺陷等）。他强调 KVM 允许用户空间写入 PMCR_EL0.N，且这种行为不会改变。

本周的讨论中，Itaru Kitayama 表示如果没有进一步的讨论，他将放弃该补丁。Marc Zyngier 则回应希望 Itaru 能提供更多的背景信息，以便讨论和解决潜在问题，而不是简单地放弃补丁。

总结来看，本周的讨论主要围绕补丁的有效性和必要性展开，尽管提出了构建失败的问题，但缺乏足够的解释和讨论，导致补丁的前景不明。

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

本邮件线程讨论了针对 ARM64 系统寄存器（sysreg）字段定义和生成脚本的修复补丁（PATCH v3 0/3）。历史讨论中，Fuad Tabba 指出 sysreg 定义文件存在多个错误，包括 Enum Security 中 NSACR_RFR 的值设置错误，以及 DoubleLock 和 EIESB 的符号定义不正确。此外，文件中还有一些冗余定义（如 RCWSMASK_EL1），虽然这些冗余定义本身并不错误，但可能会导致未来的代码问题。

在本周的新讨论中，Fuad Tabba 重申了补丁的内容，强调了对枚举和冗余定义的修复，并提出了在 sysreg 头文件生成脚本中添加验证功能，以减少未来出现类似错误的可能性。他还更新了补丁，修正了 DoubleLock 和 EIESB 的符号定义，并移除了不必要的空格修复。最后，Will Deacon 确认已将补丁应用到 ARM64 的开发分支中，并提供了每个补丁的链接。

总结来看，本周的讨论主要集中在补丁的确认和应用上，确保了 sysreg 定义的准确性和生成脚本的可靠性。

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

本邮件讨论的主题是针对 ARM64 架构的 futex 机制中的一个小优化补丁（PATCH v7 RESEND 5/6），具体针对函数 `__llsc_futex_atomic_set()`。该补丁旨在通过减少一条指令来提升性能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是基于对现有代码的性能分析，试图在频繁修改的代码中实现小幅度的优化。

在本周的新讨论中，参与者对该补丁的必要性和可维护性进行了深入探讨。Will Deacon 表示对这个优化的有效性持怀疑态度，认为增加新的汇编代码并未显著提升可维护性。Yeoreum Yun 也表达了类似的看法，虽然他认为小优化可能有益，但并没有强烈支持该补丁，甚至表示如果从可维护性角度看不佳，可以考虑放弃。Catalin Marinas 则建议在没有明确性能提升证据的情况下，暂时搁置该补丁。

总体而言，本周的讨论反映出对该补丁的质疑，参与者倾向于在没有明显性能收益的情况下不推进此优化。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 TWED（Trap Watchpoint Exception Descriptor）配置的补丁。补丁的主要内容是：在 TWE（Trap Watchpoint Enable）未设置的情况下，排除来宾的 TWED 配置，以避免潜在地延迟主机所需的陷阱。

在之前的讨论中，Oliver Upton 提出了该补丁，指出 KVM 在处理来宾值时会盲目地将 TWEDEL 和 TWEDEn 的值与编程值进行或运算，即使来宾已禁用 WFE（Wait For Event）陷阱。为了解决这个问题，补丁建议在 TWE 未设置时排除这些字段。

本周的新讨论中，Marc Zyngier 对补丁提出了疑问，认为在当前的实现中，ID_AA64MMFR1_EL1 被清理到完全移除 TWED 特性，因此 HCR_EL2 中的 TWEDEn 和 TWEDEL 应该为 0。他询问是否还有其他方式让来宾设置这些位。对此，Oliver Upton 解释说，他未检查限制条件，计划在后续版本中放宽这些限制。

总结而言，本周的讨论主要集中在补丁的合理性和实现细节上，参与者们对如何处理 TWED 配置进行了深入的探讨。

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

本邮件讨论的主题是关于在 pKVM/nvhe 中处理内核崩溃时转储指令的补丁（PATCH）。该补丁旨在增强调试能力，特别是在内存损坏的情况下。

**原始补丁内容**：补丁分为两部分。第一部分针对 nvhe，允许在内核崩溃时转储故障指令，类似于内核的处理方式。第二部分则为 pKVM 提供支持，涉及到将 hypervisor 代码映射为只读（RO），以便在崩溃时能够提取调试信息。

**之前讨论要点**：在历史讨论中，参与者讨论了如何在崩溃时有效地转储指令，并考虑了不同的实现方案。补丁的设计经过了反馈和修改，以增强指令转储的安全性和可靠性。

**本周新讨论与进展**：本周的讨论中，Mostafa Saleh 提交了补丁的第二版，进一步细化了对 nvhe 和 pKVM 的支持，确保在崩溃时可以正确转储指令。此外，补丁得到了 Kunwu Chan 的测试和审核，Will Deacon 也对此表示认可。整体来看，本周的进展主要集中在补丁的细节调整和增强功能上，为后续的合并做好准备。

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

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构中 vgic（虚拟中断控制器）代码的一个补丁，旨在修复不正确的自旋锁 API 使用。

**原始补丁内容**：Alok Tiwari 提出的补丁指出，函数 vgic_flush_lr_state() 错误地调用了低级 API _raw_spin_unlock()，而应使用更合适的 raw_spin_unlock()。该补丁的目的是替换低级 API 的使用，以确保在 vgic 代码中遵循正确的锁定语义，并与内核锁定约定保持一致。

**之前讨论要点**：在历史讨论中，Alok 强调了使用低级 API 的潜在问题，并指出此补丁可以避免对内部函数的误用，提升代码的可维护性和安全性。

**本周新讨论进展**：在本周的讨论中，Marc Zyngier 对补丁进行了反馈，建议对某些表述进行修改，并表示支持该补丁（Acked-by）。Alok 随后确认将根据 Marc 的建议提交补丁的第二版（v2）。

总体而言，本周的讨论推进了补丁的完善，参与者之间的互动表明对代码质量的重视。

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

本邮件线程讨论的主题是关于支持 FEAT_LSUI 并将其应用于 futex 原子操作的补丁（patch）。该补丁旨在增强 Linux 内核在处理原子操作时的性能。

在历史讨论中，参与者们主要关注 FEAT_LSUI 的具体实现细节及其在当前架构文档中的可用性。然而，邮件中并未提供具体的历史讨论内容。

在本周的新讨论中，Will Deacon 提出了对 FEAT_LSUI 的架构规范的查询，表示在最新的 Arm ARM 文档中找不到相关细节。Catalin Marinas 随后回应，指出目前该信息仅在公共 XML 文档中可用，预计在年底前会有 Arm ARM 的正式发布，否则只能参考私有的 2024 架构规范。他表示，如果参与者希望等待公共文档的发布，完全可以这样做。

总体来看，本周的讨论主要集中在 FEAT_LSUI 的文档可用性上，尚未对补丁本身的具体实现或效果进行深入讨论。

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

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 VBAR_EL1 参数顺序的问题。

1. **原始补丁内容**：补丁由 Fuad Tabba 提交，主要修正了 `__vcpu_assign_sys_reg()` 函数调用中参数的顺序。该函数期望第二个参数为寄存器 ID，第三个参数为要赋值的值，而原有代码传递的顺序不正确。补丁确保在处理异常之前，虚拟 CPU（vCPU）能够正确读取和更新来自来宾的 VBAR_EL1 值，以确保异常在恢复来宾时能在正确的地址处理。

2. **之前的讨论要点**：本邮件线程没有提供历史讨论的具体内容，直接进入了本周的新讨论。

3. **本周的新讨论和进展**：在本周的讨论中，Fuad Tabba 提交的补丁得到了 Oliver Upton 的确认，并已应用到修复列表中。这标志着该问题的修复已被接受并将纳入后续的代码更新。

总的来说，本周的讨论集中在修复 KVM arm64 的参数顺序问题上，补丁已成功应用，确保了系统的稳定性和正确性。

#### 📝 邮件列表

1. **[09-08 17:35]** [PATCH] KVM: arm64: Fix parameter ordering for VBAR_EL1 assignment
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[09-08 11:23]** Re: [PATCH] KVM: arm64: Fix parameter ordering for VBAR_EL1 assignment
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 26: [PATCH v2] KVM: arm64: Remove stage 2 read fault check

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  8 Sep 2025 14:48:06 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是移除 stage 2 读取故障检查。

1. **原始补丁内容**：补丁的核心是移除对 stage 2 读取权限的检查。在非 NV（Non-Virtualization）情况下，映射 stage 2 时始终授予读取权限，因此进行此检查没有实际意义。而在 NV 客户端的情况下，shadow stage 2 可能会有非可读的映射，因此在这种情况下也不应检查读取故障。

2. **之前讨论要点**：虽然邮件中没有详细的历史讨论记录，但补丁的建议者包括 Oliver Upton 和 Marc Zyngier，他们的参与表明该补丁经过了一定的讨论和验证。

3. **本周的新讨论与进展**：在本周的讨论中，Wei-Lin Chang 提交了补丁的 v2 版本，并明确指出移除了读取故障检查。Oliver Upton 对该补丁表示认可，并已将其应用于修复列表中，确认了补丁的有效性。

总体来看，此次讨论集中在简化 KVM 的代码逻辑上，提升了代码的清晰度和效率。

#### 📝 邮件列表

1. **[09-08 14:48]** [PATCH v2] KVM: arm64: Remove stage 2 read fault check
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[09-08 11:23]** Re: [PATCH v2] KVM: arm64: Remove stage 2 read fault check
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 27: [PATCH v2] KVM: arm64: vgic: fix incorrect spinlock API usage

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  8 Sep 2025 11:04:11 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic（虚拟通用中断控制器）代码的补丁。补丁的主要目的是修复在函数 `vgic_flush_lr_state()` 中错误使用了低级 API `_raw_spin_unlock()`，而应使用更合适的 `raw_spin_unlock()`，以确保在 vgic 代码中正确的锁定语义。

在之前的讨论中，补丁的作者 Alok Tiwari 指出，使用 `_raw_spin_unlock()` 可能导致锁定行为不符合预期，因此需要进行修正。补丁的修订版本（v2）中，作者删除了多余的段落，并添加了来自 Marc Zyngier 的确认（Acked-by），以增强补丁的有效性。

在本周的新讨论中，Alok Tiwari 提交了补丁并确认已被应用到修复列表中。Oliver Upton 对此表示感谢，并确认补丁已成功合并。这表明该问题得到了及时解决，相关代码也得到了改进。

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

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构中使用 SMCCC 1.2 进行 FF-A（Firmware Framework for Arm）初始化的补丁（patch）——[PATCH v11 2/6]。该补丁旨在改进 KVM 的主机处理程序，使其更好地支持 FF-A 1.2。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是 KVM 对 FF-A 支持的系列更新的一部分，可能涉及到对 ARM 架构虚拟化的增强。

在本周的新讨论中，参与者 Will Deacon 对该补丁表示认可，并确认其看起来一切正常。他提到，如果另一位参与者 Marc 也满意，那么该补丁将通过 kvmarm 树进行合并。这表明补丁得到了积极的反馈，并且即将进入下一步的整合流程。

总的来说，本周的讨论主要集中在对补丁的认可和即将合并的确认上，显示出对 KVM 在 arm64 上支持 FF-A 的持续推进。

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

本邮件主题为“[PATCH RESEND v7 2/6] KVM: arm64: expose FEAT_LSUI to guest”，主要讨论了在 KVM（Kernel-based Virtual Machine）中对 ARM64 架构的虚拟机客户机暴露 FEAT_LSUI 特性的问题。

在历史讨论中，虽然没有具体的邮件记录，但可以推测此 patch 的目的是为了增强 ARM64 客户机的功能，使其能够利用 FEAT_LSUI 特性。这一特性可能与内存访问或指令集扩展相关，旨在提升虚拟化性能或兼容性。

在本周的新讨论中，参与者 Catalin Marinas 对该 patch 进行了审查，并表示支持，标记为“Reviewed-by”。这表明该 patch 在技术上得到了认可，可能会在后续版本中被合并。

总体来看，本周的进展主要是对该 patch 的审查反馈，显示出社区对增强 KVM 功能的积极态度。

#### 📝 邮件列表

1. **[09-12 17:25]** Re: [PATCH RESEND v7 2/6] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 30: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 12 Sep 2025 17:24:11 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig”，主要讨论了在 arm64 架构的 Kconfig 中添加 LSUI（Load Store Unit Instruction）支持的补丁。

在历史讨论中，没有提供具体的背景信息，因此我们无法了解该补丁的详细内容或之前的讨论要点。

在本周的新讨论中，参与者 Catalin Marinas 对补丁进行了审查，并提出了一些建议。他指出补丁的主题可以稍作改进，以更清晰地表述其目的是检测工具链对 LSUI 的支持。此外，他提到 binutils 2.45 已经添加了对 LSUI 的支持，并建议在帮助信息中使用两个空格的缩进格式。总体而言，Catalin 对补丁的内容表示认可，并给予了“Reviewed-by”的标记，表明他支持该补丁的提交。

总结来看，本周的讨论主要集中在补丁的细节改进上，未涉及更广泛的历史背景或其他参与者的反馈。

#### 📝 邮件列表

1. **[09-12 17:24]** Re: [PATCH RESEND v7 3/6] arm64: Kconfig: add LSUI Kconfig
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 31: [PATCH RESEND v7 1/6] arm64: cpufeature: add FEAT_LSUI

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 12 Sep 2025 17:12:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁，内容为添加 CPU 特性检测功能 FEAT_LSUI。该补丁的目的是增强 ARM64 架构中对特定 CPU 特性的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改善 CPU 特性检测的能力，可能涉及到 PSTATE.PAN 的相关功能。

在本周的新讨论中，参与者 Catalin Marinas 对补丁进行了审查，提出了建议。他指出补丁中的两个段落内容重复，建议将第二段简化为“添加对 FEAT_LSUI 的 CPU 特性检测”，认为无需再次解释 PSTATE.PAN 的内容。最终，Catalin Marinas 表示支持该补丁，给予了“Reviewed-by”的标记，表明他对补丁的认可。

总的来说，本周的讨论主要集中在补丁的表述优化上，未涉及新的技术争议或问题。

#### 📝 邮件列表

1. **[09-12 17:12]** Re: [PATCH RESEND v7 1/6] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 32: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 08 Sep 2025 19:42:57 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容为“[PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception”，主要涉及在进入异常时设置 PSTATE.EXLOCK 的问题。

在历史讨论中，并没有提供具体的背景信息或之前的讨论内容，因此我们无法了解该补丁的详细背景或相关的技术争议。

本周的新讨论中，Marc Zyngier 对补丁进行了回复，指出在 ARM 架构参考手册中可以去掉某个章节编号，因为这些编号在文档的不同版本中是稳定的。此外，他提到目前只有 NV 是需要模拟 ERET 的情况。这表明补丁的实现可能与异常处理相关，并且在特定情况下需要进行额外的处理。

总体来看，本周的讨论主要集中在补丁的细节和文档规范上，尚未有进一步的技术争议或进展。

#### 📝 邮件列表

1. **[09-08 19:42]** Re: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 33: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside
 other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 8 Sep 2025 15:19:00 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 ptdump 功能的一个补丁（patch）。该补丁的主要内容是建议在检查页表项（PTE）时，不要同时测试 PTE_VALID 和其他属性，以提高代码的清晰度和效率。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于对现有代码的审查和优化需求提出的，旨在简化逻辑并减少潜在的错误。

在本周的新讨论中，Will Deacon 对该补丁表示认可，并确认将由 Oliver 或 Marc 通过 kvmarm 树来处理此补丁。这表明补丁得到了社区的支持，并将进入后续的开发流程。整体来看，本周的进展是补丁获得了确认，并将继续推进。

#### 📝 邮件列表

1. **[09-08 15:19]** Re: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside
 other attributes
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 34: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 8 Sep 2025 14:25:18 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH kvmtool v3 0/6] arm64: Nested virtualization support”，主要讨论了对 arm64 架构的嵌套虚拟化支持的补丁。邮件中提到的补丁包含六个部分，旨在增强 KVM 工具对嵌套虚拟化的支持。

在历史讨论中，虽然没有具体的邮件内容提供，但可以推测之前的讨论涉及对该补丁的初步反馈和改进建议，尤其是 Alexandru 提出的未解决评论。

在本周的新讨论中，Will Deacon 向 Andre Przywara 提出询问，询问他是否计划根据 Alexandru 的评论重新提交补丁。这表明该补丁仍在审查过程中，且开发者们关注如何进一步完善和解决之前的反馈意见。

总体来看，本周的讨论主要集中在补丁的后续进展和对先前评论的响应上，显示出开发者们对改进嵌套虚拟化支持的持续关注。

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

本邮件线程讨论了一个关于在 ARM64 环境中验证 MMIO（内存映射输入输出）范围的补丁（RFC PATCH v1 34/38）。该补丁旨在解决在接口报告中发现的 MMIO 范围验证问题。

在之前的讨论中，参与者指出，当前的 RSI_VDEV_VALIDATE_MAPPING 接口存在缺陷，无法正确处理来自 TDISP 报告的数据格式，导致设备驱动在映射 MMIO 时可能会出现安全性问题。特别是，当一个 BAR（基地址寄存器）包含稀疏的区域（如 TEE 页面和 MSI-X 表）时，接口报告可能会包含多个具有相同范围 ID 的范围，导致验证失败。

本周的新讨论中，Arto Merilainen 重新审视了他的建议，认为需要更通用的解决方案来处理 MSI-X 表和 PBA 范围的问题。Jason Gunthorpe 提出，内核应确保驱动不会错误地映射不安全的 MMIO 区域。Aneesh Kumar K.V 询问是否可以假设接口报告中仅缺少 MSI-X 表和 PBA 范围，并建议从配置空间中检索 MSI-X 的真实地址以正确映射 BAR 的起始位置。其他参与者也讨论了如何在 PCI/TSM 核心中处理 MMIO 范围的标记问题，强调需要建立通用基础设施来处理特殊情况。

总体来看，讨论集中在如何确保 MMIO 范围的安全性和准确性，以及如何改进现有的验证机制。

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

本邮件线程讨论了在 KVM (Kernel-based Virtual Machine) 的 ARM64 架构中，vgic_put_irq 函数存在的锁定错误问题。历史讨论中，syzbot 提出了该问题，并提供了相关的内核提交信息和日志链接，指出在特定的内核版本中出现了该警告。

在之前的讨论中，参与者关注了该锁定错误的影响，并探讨了可能的解决方案。邮件中提到的原始 patch 旨在修复该锁定问题，但具体的实现细节未在历史讨论中详细展开。

在本周的新讨论中，Oliver Upton 提出了对该问题的进一步测试请求，试图验证修复效果。然而，syzbot 报告了在测试过程中遇到的构建和启动失败，主要是由于在尝试将二进制文件复制到虚拟机时连接超时。尽管进行了多次尝试，但最终未能成功应用任何补丁，导致测试未能完成。

总结来看，尽管有针对锁定错误的修复 patch 提出，但在实际测试中遇到的连接问题阻碍了进一步的验证和进展。

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

本邮件讨论了 KVM/arm64 在 6.17 版本中的最新变更，主要由 Oliver Upton 提出。这是针对 6.17 的第三轮修复，可能是最终的修复集。

在历史讨论中，没有提供具体的背景信息，但本周的邮件指出，之前在 6.17 中引入的一些修复因存在引用计数和使用后释放（UAF）问题而被撤回。这些问题出现在处理阶段 2 页表销毁时，之前的临时解决方案未能有效解决这些问题。

本周的讨论中，Oliver 提到了一系列修复，包括：
1. 在释放 PGD 时使嵌套 MMU 无效，以避免在访问 MMU 通知时产生警告。
2. 修复 TLB 匹配过程和 TLB 无效范围，以管理 VCNR 伪 TLB。
3. 防止 SPE 错误地分析来宾的情况。
4. 修正 VGIC LPIs 的锁定顺序，避免嵌套锁定的场景。
5. 允许在某些情况下发生阶段 2 读取权限中止。

此外，还进行了其他一些小的修复和改进，包括对 VBAR_EL1 的参数顺序修正等。总的来说，本周的讨论集中在解决之前引入的缺陷和进一步优化 KVM/arm64 的实现上。

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

本邮件讨论主题为修复 ARM64 架构下 MTE（Memory Tagging Extension）粒度掩码的补丁。历史讨论中，Vladimir Murzin 提出了一个补丁，旨在确保在与 MTE_TAG_SHIFT 一起使用时生成正确的掩码。补丁修改了 MTE_GRANULE_MASK 的定义，从原来的取反形式改为直接使用粒度大小减一的值，以确保掩码正确。

在本周的新讨论中，参与者 Alexandru Elisei 对补丁的使用进行了详细分析，确认了补丁的正确性，并指出在修改前后掩码的变化。Vladimir Murzin 也回应了 Alexandru 的问题，解释了他是如何通过目测发现问题的。最后，Andrew Jones 表示已将该补丁合并，标志着讨论的结束。

总结来说，此次讨论围绕 MTE 粒度掩码的修复展开，补丁已获得认可并成功合并。

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

本邮件线程讨论了一个由 syzbot 报告的 KASAN（Kernel Address Sanitizer）错误，具体是发生在 `__kvm_pgtable_walk` 函数中的无效内存访问问题。该问题的详细信息包括错误发生的代码位置、相关的内存地址和调用栈信息。

在历史讨论中，虽然没有具体的历史邮件记录，但可以推测该问题与 KVM（Kernel-based Virtual Machine）在 ARM 架构下的页面表处理有关。错误报告指出，内存访问违规可能与 KVM 的页面表遍历逻辑有关，尤其是在处理虚拟机的内存管理时。

在本周的新讨论中，Oliver Upton 提出了一个测试补丁的建议，试图解决该问题。然而，syzbot 测试后发现，该补丁并未解决问题，错误依然存在，且新的错误信息显示在 `__kvm_pgtable_walk` 函数中再次触发了 KASAN 报告。这表明当前的修复措施未能有效解决内存访问违规的问题，后续可能需要进一步的调试和修复工作。

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

本邮件讨论的主题是关于在 KVM ARM64 环境中发生的内核崩溃（kernel panic）问题，具体表现为“未处理的异常”（Unhandled exception）。这是由 syzbot 发现的一个问题，相关的内核版本为 9c642e6226e3。

在历史讨论中没有相关的背景信息，因此本周的讨论是首次提出此问题。邮件中提供了详细的崩溃信息，包括调用栈和锁状态的不一致警告，显示在执行 KVM 虚拟机初始化时发生了内核崩溃。具体的崩溃信息显示，系统在处理某些锁时出现了潜在的死锁情况，导致无法正常同步。

本周的讨论主要集中在该问题的详细日志和重现步骤上，提供了多个链接以供开发者查看相关的日志、配置和重现代码。syzkaller 还建议如果有人修复了此问题，请在提交补丁时添加相应的标签以便追踪。

总结来说，本周的讨论首次揭示了 KVM ARM64 环境中的内核崩溃问题，并提供了详细的调试信息，期待后续的修复和进一步的讨论。

#### 📝 邮件列表

1. **[09-09 10:52]** [syzbot] [kvmarm?] kernel panic: Unhandled exception
   - 发件人: syzbot <syzbot+d173b3985bd6b9487fa1@syzkaller.appspotmail.com>

---

