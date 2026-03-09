# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-03-09 00:30:13

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 352
- **总 Thread 数**: 36
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 33 threads (341 邮件)
- **Bug Report**: 1 threads (4 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Other**: 1 threads (6 邮件)

---

## 📌 PATCH

共 33 个 thread

---

### Thread 1: [PATCH v3 00/36] KVM: arm64: Add support for protected guest memory with pKVM

**📧 邮件数**: 37 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  5 Mar 2026 14:43:13 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上实现受保护虚拟机（pKVM）的补丁集（PATCH v3 00/36）。该补丁集的主要目的是为虚拟机提供内存保护和隔离功能，以增强安全性。

1. **原始补丁/问题内容**：
   本次补丁集的核心是为 KVM 添加对受保护虚拟机的支持，允许在 ARM64 上实现内存保护机制。补丁包括多个方面的改进，例如异常处理、内存捐赠、共享和取消共享内存等功能。

2. **之前讨论要点**：
   之前的讨论集中在如何实现内存的捐赠和回收机制，确保虚拟机的内存隔离，以及如何处理来自受保护虚拟机的异常和超调用（hypercall）。补丁集的设计考虑了性能和安全性，确保在不同情况下的内存访问不会导致系统崩溃。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要集中在补丁的具体实现上，包括：
   - 引入新的超调用以支持受保护虚拟机的内存共享和取消共享。
   - 实现了强制回收捐赠内存的超调用，确保在虚拟机崩溃或异常情况下能够安全地回收内存。
   - 扩展了自测试，以涵盖新的内存捐赠和共享功能，确保这些功能在实际使用中的可靠性。
   - 添加了文档，帮助用户理解 pKVM 的功能和限制。

总的来说，本次补丁集的实施将为 KVM 提供更强的内存保护能力，增强虚拟机的安全性，同时也为未来的开发奠定了基础。

#### 📝 邮件列表

1. **[03-05 14:43]** [PATCH v3 00/36] KVM: arm64: Add support for protected guest memory with pKVM
   - 发件人: Will Deacon <will@kernel.org>
2. **[03-05 14:43]** [PATCH v3 01/36] KVM: arm64: Don't leak stage-2 page-table if VM fails to init under pKVM
   - 发件人: Will Deacon <will@kernel.org>
3. **[03-05 14:43]** [PATCH v3 02/36] KVM: arm64: Move handle check into pkvm_pgtable_stage2_destroy_range()
   - 发件人: Will Deacon <will@kernel.org>
4. **[03-05 14:43]** [PATCH v3 03/36] KVM: arm64: Rename __pkvm_pgtable_stage2_unmap()
   - 发件人: Will Deacon <will@kernel.org>
5. **[03-05 14:43]** [PATCH v3 04/36] KVM: arm64: Don't advertise unsupported features for protected guests
   - 发件人: Will Deacon <will@kernel.org>
6. **[03-05 14:43]** [PATCH v3 05/36] KVM: arm64: Expose self-hosted debug regs as RAZ/WI for protected guests
   - 发件人: Will Deacon <will@kernel.org>
7. **[03-05 14:43]** [PATCH v3 06/36] KVM: arm64: Remove is_protected_kvm_enabled() checks from hypercalls
   - 发件人: Will Deacon <will@kernel.org>
8. **[03-05 14:43]** [PATCH v3 07/36] KVM: arm64: Ignore MMU notifier callbacks for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
9. **[03-05 14:43]** [PATCH v3 08/36] KVM: arm64: Prevent unsupported memslot operations on protected VMs
   - 发件人: Will Deacon <will@kernel.org>
10. **[03-05 14:43]** [PATCH v3 09/36] KVM: arm64: Ignore -EAGAIN when mapping in pages for the pKVM host
   - 发件人: Will Deacon <will@kernel.org>
11. **[03-05 14:43]** [PATCH v3 10/36] KVM: arm64: Split teardown hypercall into two phases
   - 发件人: Will Deacon <will@kernel.org>
12. **[03-05 14:43]** [PATCH v3 11/36] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Will Deacon <will@kernel.org>
13. **[03-05 14:43]** [PATCH v3 12/36] KVM: arm64: Hook up donation hypercall to pkvm_pgtable_stage2_map()
   - 发件人: Will Deacon <will@kernel.org>
14. **[03-05 14:43]** [PATCH v3 13/36] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
15. **[03-05 14:43]** [PATCH v3 14/36] KVM: arm64: Introduce __pkvm_reclaim_dying_guest_page()
   - 发件人: Will Deacon <will@kernel.org>
16. **[03-05 14:43]** [PATCH v3 15/36] KVM: arm64: Hook up reclaim hypercall to pkvm_pgtable_stage2_destroy()
   - 发件人: Will Deacon <will@kernel.org>
17. **[03-05 14:43]** [PATCH v3 16/36] KVM: arm64: Factor out pKVM host exception injection logic
   - 发件人: Will Deacon <will@kernel.org>
18. **[03-05 14:43]** [PATCH v3 17/36] KVM: arm64: Support translation faults in inject_host_exception()
   - 发件人: Will Deacon <will@kernel.org>
19. **[03-05 14:43]** [PATCH v3 18/36] KVM: arm64: Inject SIGSEGV on illegal accesses
   - 发件人: Will Deacon <will@kernel.org>
20. **[03-05 14:43]** [PATCH v3 19/36] KVM: arm64: Avoid pointless annotation when mapping host-owned pages
   - 发件人: Will Deacon <will@kernel.org>
21. **[03-05 14:43]** [PATCH v3 20/36] KVM: arm64: Generalise kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
22. **[03-05 14:43]** [PATCH v3 21/36] KVM: arm64: Introduce host_stage2_set_owner_metadata_locked()
   - 发件人: Will Deacon <will@kernel.org>
23. **[03-05 14:43]** [PATCH v3 22/36] KVM: arm64: Change 'pkvm_handle_t' to u16
   - 发件人: Will Deacon <will@kernel.org>
24. **[03-05 14:43]** [PATCH v3 23/36] KVM: arm64: Annotate guest donations with handle and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
25. **[03-05 14:43]** [PATCH v3 24/36] KVM: arm64: Introduce hypercall to force reclaim of a protected page
   - 发件人: Will Deacon <will@kernel.org>
26. **[03-05 14:43]** [PATCH v3 25/36] KVM: arm64: Reclaim faulting page from pKVM in spurious fault handler
   - 发件人: Will Deacon <will@kernel.org>
27. **[03-05 14:43]** [PATCH v3 26/36] KVM: arm64: Return -EFAULT from VCPU_RUN on access to a poisoned pte
   - 发件人: Will Deacon <will@kernel.org>
28. **[03-05 14:43]** [PATCH v3 27/36] KVM: arm64: Add hvc handler at EL2 for hypercalls from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
29. **[03-05 14:43]** [PATCH v3 28/36] KVM: arm64: Implement the MEM_SHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
30. **[03-05 14:43]** [PATCH v3 29/36] KVM: arm64: Implement the MEM_UNSHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
31. **[03-05 14:43]** [PATCH v3 30/36] KVM: arm64: Allow userspace to create protected VMs when pKVM is enabled
   - 发件人: Will Deacon <will@kernel.org>
32. **[03-05 14:43]** [PATCH v3 31/36] KVM: arm64: Add some initial documentation for pKVM
   - 发件人: Will Deacon <will@kernel.org>
33. **[03-05 14:43]** [PATCH v3 32/36] KVM: arm64: Extend pKVM page ownership selftests to cover guest donation
   - 发件人: Will Deacon <will@kernel.org>
34. **[03-05 14:43]** [PATCH v3 33/36] KVM: arm64: Register 'selftest_vm' in the VM table
   - 发件人: Will Deacon <will@kernel.org>
35. **[03-05 14:43]** [PATCH v3 34/36] KVM: arm64: Extend pKVM page ownership selftests to cover forced reclaim
   - 发件人: Will Deacon <will@kernel.org>
36. **[03-05 14:43]** [PATCH v3 35/36] KVM: arm64: Extend pKVM page ownership selftests to cover guest hvcs
   - 发件人: Will Deacon <will@kernel.org>
37. **[03-05 14:43]** [PATCH v3 36/36] KVM: arm64: Rename PKVM_PAGE_STATE_MASK
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 2: [PATCH v13 00/32] Tracefs support for pKVM

**📧 邮件数**: 34 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Mar 2026 14:35:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（PATCH v13 00/32），主要集中在引入远程跟踪功能，以便在虚拟化环境中进行调试和性能分析。

1. **原始补丁/问题内容**：
   该补丁系列旨在为 pKVM 超级管理程序引入 Tracefs 支持，允许内核通过 Tracefs 读取由超管（如固件或虚拟机监控程序）写入的环形缓冲区。补丁中定义了新的接口和结构，以便在内核和超管之间共享跟踪事件。

2. **之前讨论要点**：
   之前的讨论集中在如何实现远程环形缓冲区的结构和接口，确保内核能够有效地读取超管生成的事件。补丁中提到的环形缓冲区设计考虑了性能和易用性，旨在简化调试过程。

3. **本周的新讨论、进展或结论**：
   本周的讨论包括多个补丁的提交，涵盖了环形缓冲区的实现、Tracefs 目录的创建、事件的定义和支持等。具体进展包括：
   - 引入了简单的环形缓冲区实现，供 pKVM 超管使用。
   - 添加了对事件的支持，允许在 Tracefs 中注册和管理事件。
   - 提交了自测模块和相关的测试用例，以验证新功能的正确性。
   - 讨论了如何在 nVHE/pKVM 超管中实现跟踪功能，包括跟踪时钟的同步和事件的记录。

总的来说，本周的工作为 pKVM 的调试和性能分析提供了重要的基础设施，增强了内核与超管之间的交互能力。

#### 📝 邮件列表

1. **[03-06 14:35]** [PATCH v13 00/32] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-06 14:35]** [PATCH v13 01/32] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-06 14:35]** [PATCH v13 02/32] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-06 14:35]** [PATCH v13 03/32] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-06 14:35]** [PATCH v13 04/32] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[03-06 14:35]** [PATCH v13 05/32] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-06 14:35]** [PATCH v13 06/32] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[03-06 14:35]** [PATCH v13 07/32] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[03-06 14:35]** [PATCH v13 08/32] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[03-06 14:35]** [PATCH v13 09/32] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[03-06 14:35]** [PATCH v13 10/32] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[03-06 14:35]** [PATCH v13 11/32] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[03-06 14:35]** [PATCH v13 12/32] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[03-06 14:35]** [PATCH v13 13/32] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[03-06 14:35]** [PATCH v13 14/32] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[03-06 14:35]** [PATCH v13 15/32] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[03-06 14:35]** [PATCH v13 16/32] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[03-06 14:35]** [PATCH v13 17/32] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[03-06 14:35]** [PATCH v13 18/32] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[03-06 14:35]** [PATCH v13 19/32] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[03-06 14:35]** [PATCH v13 20/32] KVM: arm64: Add clock support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[03-06 14:35]** [PATCH v13 21/32] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[03-06 14:35]** [PATCH v13 22/32] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[03-06 14:35]** [PATCH v13 23/32] KVM: arm64: Add tracing capability for the
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[03-06 14:35]** [PATCH v13 24/32] KVM: arm64: Add trace remote for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[03-06 14:35]** [PATCH v13 25/32] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[03-06 14:35]** [PATCH v13 26/32] KVM: arm64: Add trace reset to the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[03-06 14:35]** [PATCH v13 27/32] KVM: arm64: Add event support to the nVHE/pKVM hyp
 and trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[03-06 14:35]** [PATCH v13 28/32] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[03-06 14:35]** [PATCH v13 29/32] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
31. **[03-06 14:35]** [PATCH v13 30/32] tracing: selftests: Add hypervisor trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
32. **[03-06 14:35]** [PATCH v13 31/32] fixup! tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
33. **[03-06 14:35]** [PATCH v13 32/32] fixup! tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
34. **[03-06 17:37]** Re: [PATCH v13 03/32] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Markus Elfring <Markus.Elfring@web.de>

---

### Thread 3: [PATCH v10 00/30] KVM: arm64: Implement support for SME

**📧 邮件数**: 31 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 06 Mar 2026 17:00:52 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现对 SME（Scalable Matrix Extension）的支持，主要涉及一系列补丁的提交和讨论。

1. **原始补丁/问题内容**：
   - 本系列补丁（PATCH v10 00/30）旨在为 KVM 实现对 SME 的支持，特别是在非保护模式下的 KVM 客户端中。SME 引入了新的向量长度和控制寄存器，类似于 SVE（Scalable Vector Extension），并提供对 ZA 矩阵寄存器和 ZT0 LUT 寄存器的访问。

2. **之前讨论要点**：
   - 之前的讨论集中在如何处理 SME 和 SVE 的寄存器访问、状态保存和恢复，以及如何在用户空间和虚拟机监控程序（VMM）之间正确配置和管理这些新寄存器。补丁中提到的许多功能和状态管理与 SVE 的处理方式相似，但也引入了新的复杂性。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论主要集中在补丁的具体实现细节上，包括对 SME 控制寄存器的支持、状态切换、异常处理、以及如何在嵌套虚拟机中暴露 SME 状态。补丁还包括对 SME 特定寄存器的用户空间访问、状态保存和恢复的实现。此外，补丁还修复了自测中的一些问题，并增加了对 SME 相关寄存器的测试覆盖。

总体而言，本周的讨论和补丁提交展示了 KVM 在 arm64 架构下对 SME 的逐步支持，涉及的技术细节和实现方法为未来的开发和维护奠定了基础。

#### 📝 邮件列表

1. **[03-06 17:00]** [PATCH v10 00/30] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[03-06 17:00]** [PATCH v10 01/30] arm64/sysreg: Update SMIDR_EL1 to DDI0601
 2025-06
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[03-06 17:00]** [PATCH v10 02/30] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[03-06 17:00]** [PATCH v10 03/30] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[03-06 17:00]** [PATCH v10 04/30] arm64/fpsimd: Determine maximum virtualisable
 SME vector length
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[03-06 17:00]** [PATCH v10 05/30] KVM: arm64: Pay attention to FFR parameter in
 SVE save and load
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[03-06 17:00]** [PATCH v10 06/30] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[03-06 17:00]** [PATCH v10 07/30] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[03-06 17:01]** [PATCH v10 08/30] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[03-06 17:01]** [PATCH v10 09/30] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[03-06 17:01]** [PATCH v10 10/30] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[03-06 17:01]** [PATCH v10 11/30] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[03-06 17:01]** [PATCH v10 12/30] KVM: arm64: Factor SVE code out of
 fpsimd_lazy_switch_to_host()
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[03-06 17:01]** [PATCH v10 13/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[03-06 17:01]** [PATCH v10 14/30] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[03-06 17:01]** [PATCH v10 15/30] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[03-06 17:01]** [PATCH v10 16/30] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[03-06 17:01]** [PATCH v10 17/30] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[03-06 17:01]** [PATCH v10 18/30] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[03-06 17:01]** [PATCH v10 19/30] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[03-06 17:01]** [PATCH v10 20/30] KVM: arm64: Support userspace access to
 streaming mode Z and P registers
   - 发件人: Mark Brown <broonie@kernel.org>
22. **[03-06 17:01]** [PATCH v10 21/30] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[03-06 17:01]** [PATCH v10 22/30] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[03-06 17:01]** [PATCH v10 23/30] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[03-06 17:01]** [PATCH v10 24/30] KVM: arm64: Handle SME exceptions
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[03-06 17:01]** [PATCH v10 25/30] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[03-06 17:01]** [PATCH v10 26/30] KVM: arm64: Provide interface for configuring
 and enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
28. **[03-06 17:01]** [PATCH v10 27/30] KVM: arm64: selftests: Remove spurious check for
 single bit safe values
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[03-06 17:01]** [PATCH v10 28/30] KVM: arm64: selftests: Skip impossible invalid
 value tests
   - 发件人: Mark Brown <broonie@kernel.org>
30. **[03-06 17:01]** [PATCH v10 29/30] KVM: arm64: selftests: Add SME system registers
 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
31. **[03-06 17:01]** [PATCH v10 30/30] KVM: arm64: selftests: Add SME to set_id_regs
 test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 4: [PATCH v5 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 30 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Feb 2026 15:55:21 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 arm64 平台引入虚拟 GICv5（vgic_v5）及其对私有中断（PPIs）支持的补丁系列（PATCH v5 00/36）。该补丁的核心内容是实现对 GICv5 的支持，初步仅限于 PPIs，后续补丁将增加对其他中断类型的支持。

在历史讨论中，Sascha Bischoff 提出了多个补丁，涵盖了 GICv5 的各个方面，包括中断类型助手的引入、PPIs 的检测与初始化、以及状态的保存和恢复等。讨论中提到，GICv5 的实现与旧版 GIC 不兼容，因此需要引入新的助手函数来处理中断类型。

在本周的新讨论中，Marc Zyngier 对多个补丁提出了改进建议，主要集中在代码的可读性和结构优化上。例如，他建议将一些函数重构为宏以提高可读性，并对补丁中的逻辑进行简化。此外，针对 GICv5 的直接注入 PPIs 和状态生成的实现，双方讨论了如何更有效地处理这些操作。

总体来看，本周的讨论主要集中在代码质量的提升和补丁细节的完善上，参与者们积极交流，推动补丁系列的进一步发展。

#### 📝 邮件列表

1. **[02-26 15:55]** [PATCH v5 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[02-26 15:57]** [PATCH v5 07/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[02-26 15:57]** [PATCH v5 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[02-26 15:58]** [PATCH v5 10/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[02-26 15:58]** [PATCH v5 12/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[02-26 15:59]** [PATCH v5 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[02-26 15:59]** [PATCH v5 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[02-26 15:59]** [PATCH v5 16/36] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[02-26 15:59]** [PATCH v5 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate
 mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[02-26 16:00]** [PATCH v5 19/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[02-26 16:00]** [PATCH v5 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[03-03 15:04]** Re: [PATCH v5 07/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-03 15:10]** Re: [PATCH v5 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[03-03 15:54]** Re: [PATCH v5 10/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[03-03 16:02]** Re: [PATCH v5 12/36] KVM: arm64: gic-v5: Add emulation for ICC_IAFFIDR_EL1 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[03-03 17:10]** Re: [PATCH v5 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp interface
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[03-03 17:21]** Re: [PATCH v5 07/36] KVM: arm64: gic: Introduce interrupt type
 helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[03-03 17:22]** Re: [PATCH v5 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on
 boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[03-03 17:49]** Re: [PATCH v5 10/36] KVM: arm64: gic-v5: Sanitize
 ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[03-03 17:54]** Re: [PATCH v5 12/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[03-04 09:26]** Re: [PATCH v5 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and save/restore
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[03-04 09:35]** Re: [PATCH v5 16/36] KVM: arm64: gic-v5: Implement direct injection of PPIs
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[03-04 10:50]** Re: [PATCH v5 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate mask
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[03-04 11:32]** Re: [PATCH v5 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[03-04 13:08]** Re: [PATCH v5 19/36] KVM: arm64: gic-v5: Implement PPI interrupt injection
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[03-04 14:21]** Re: [PATCH v5 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for GICv5
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[03-04 14:21]** Re: [PATCH v5 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[03-04 17:38]** Re: [PATCH v5 17/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and
 generate mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[03-05 11:22]** Re: [PATCH v5 16/36] KVM: arm64: gic-v5: Implement direct injection
 of PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[03-05 13:35]** Re: [PATCH v5 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 5: [PATCH v2 00/11] arm64: Fully disable configured-out features

**📧 邮件数**: 22 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  2 Mar 2026 11:56:41 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁系列，旨在完全禁用在编译时配置的特性，以减少内核对这些特性的处理复杂性。补丁的主要内容包括对特性处理逻辑的改进，确保在编译时禁用的特性不会在内核中暴露，从而避免潜在的状态泄漏。

在历史讨论中，Marc Zyngier 提出了补丁的初版，经过 Fuad 和 Suzuki 的审查，补丁进行了多项修改，包括将某些特性标记为不兼容、在次级启动路径中不更新被覆盖的特性，以及引入新的辅助函数来设置特性字段的安全值等。

在本周的新讨论中，Marc 提交了补丁的第二版，并逐一介绍了每个补丁的功能和目的。参与者对补丁进行了审查并给予了认可，包括对特性字段更新逻辑的改进和新宏 FTR_CONFIG() 的引入，以更清晰地定义特性在启用和禁用时的行为。Fuad 还提出了一些建议，如添加修复标签和考虑其他特性字段的处理。

整体来看，本周讨论的重点在于补丁的细节审查和对特性处理逻辑的进一步优化，参与者积极反馈并确认了补丁的有效性。

#### 📝 邮件列表

1. **[03-02 11:56]** [PATCH v2 00/11] arm64: Fully disable configured-out features
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-02 11:56]** [PATCH v2 01/11] arm64: Skip update of an idreg field affected by an override
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-02 11:56]** [PATCH v2 02/11] arm64: Add a helper setting a feature field to its safe value
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-02 11:56]** [PATCH v2 03/11] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[03-02 11:56]** [PATCH v2 04/11] arm64: Convert CONFIG_ARM64_PTR_AUTH to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-02 11:56]** [PATCH v2 05/11] arm64: Convert CONFIG_ARM64_SVE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-02 11:56]** [PATCH v2 06/11] arm64: Convert CONFIG_ARM64_SME to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[03-02 11:56]** [PATCH v2 07/11] arm64: Convert CONFIG_ARM64_GCS to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[03-02 11:56]** [PATCH v2 08/11] arm64: Convert CONFIG_ARM64_MTE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[03-02 11:56]** [PATCH v2 09/11] arm64: Convert CONFIG_ARM64_POE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-02 11:56]** [PATCH v2 10/11] arm64: Convert CONFIG_ARM64_BTI to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-02 11:56]** [PATCH v2 11/11] arm64: Remove FTR_VISIBLE_IF_IS_ENABLED()
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-02 13:05]** Re: [PATCH v2 01/11] arm64: Skip update of an idreg field affected by
 an override
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[03-02 13:14]** Re: [PATCH v2 01/11] arm64: Skip update of an idreg field affected by
 an override
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[03-02 13:24]** Re: [PATCH v2 02/11] arm64: Add a helper setting a feature field to
 its safe value
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
16. **[03-02 13:24]** Re: [PATCH v2 01/11] arm64: Skip update of an idreg field affected by
 an override
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
17. **[03-02 13:35]** Re: [PATCH v2 03/11] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
18. **[03-02 13:41]** Re: [PATCH v2 02/11] arm64: Add a helper setting a feature field to
 its safe value
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[03-02 13:47]** Re: [PATCH v2 01/11] arm64: Skip update of an idreg field affected by an override
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[03-02 14:57]** Re: [PATCH v2 03/11] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[03-02 15:14]** Re: [PATCH v2 08/11] arm64: Convert CONFIG_ARM64_MTE to FTR_CONFIG()
   - 发件人: Fuad Tabba <tabba@google.com>
22. **[03-02 18:07]** Re: [PATCH v2 00/11] arm64: Fully disable configured-out features
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 6: [PATCH v10 01/15] set_memory: set_direct_map_* to take address

**📧 邮件数**: 19 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 5 Mar 2026 18:23:25 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 Linux 内核的补丁（PATCH v10 01/15），其主要内容是修改 `set_memory` 函数，使其能够接受地址作为参数。该补丁旨在改进内存管理，尤其是在处理直接映射时的灵活性。

在之前的讨论中，参与者们关注了补丁的命名和代码结构，提出了关于局部变量命名和类型转换的建议。David Hildenbrand 表达了对补丁的支持，并希望能得到其他架构维护者的确认。

本周的新讨论中，David Hildenbrand 和 Nikita Kalyazin 继续探讨了补丁的细节，包括对 `folio_{zap, restore}_direct_map` 辅助函数的添加，以支持从直接映射中移除 guest_memfd folios。Kalyazin 提出了对现有代码的改进建议，询问是否可以将某些函数合并以减少重复代码。Hildenbrand 也对不同架构的处理方式进行了讨论，强调了在实现时可能需要的特定行为。

总体来看，本周的讨论集中在补丁的实现细节和潜在的优化上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[03-05 18:23]** Re: [PATCH v10 01/15] set_memory: set_direct_map_* to take address
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
2. **[03-05 18:34]** Re: [PATCH v10 02/15] set_memory: add folio_{zap,restore}_direct_map
 helpers
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
3. **[03-05 20:07]** Re: [PATCH v10 04/15] mm/gup: drop local variable in
 gup_fast_folio_allowed
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
4. **[03-05 20:08]** Re: [PATCH v10 07/15] KVM: x86: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
5. **[03-05 20:08]** Re: [PATCH v10 08/15] KVM: arm64: define
 kvm_arch_gmem_supports_no_direct_map()
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
6. **[03-05 20:18]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
7. **[03-06 12:48]** Re: [PATCH v10 01/15] set_memory: set_direct_map_* to take address
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
8. **[03-06 12:48]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
9. **[03-06 12:49]** Re: [PATCH v10 04/15] mm/gup: drop local variable in
 gup_fast_folio_allowed
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
10. **[03-06 12:49]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
11. **[03-06 15:17]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
12. **[03-06 15:22]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
13. **[03-06 14:48]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
14. **[03-06 14:49]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
15. **[03-06 16:16]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
16. **[03-06 16:17]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>
17. **[03-06 15:41]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
18. **[03-06 15:42]** Re: [PATCH v10 09/15] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
19. **[03-06 21:06]** Re: [PATCH v10 02/15] set_memory: add folio_{zap, restore}_direct_map
 helpers
   - 发件人: David Hildenbrand (Arm) <david@kernel.org>

---

### Thread 7: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 17 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 24 Feb 2026 17:56:39 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH v5 00/41] arm_mpam: 添加 KVM/arm64 和 resctrl 的粘合代码”，主要涉及对 ARM MPAM（内存带宽分区管理）的支持和相关补丁的讨论。

**原始补丁内容**：
该补丁系列的主要变化是更新 CDP（Cache Domain Partitioning）仿真以匹配 resctrl 接口，允许单独启用 L2 和 L3 资源的 CDP。补丁还包括对 MPAM 相关寄存器的处理和配置，以确保在 KVM 环境中正确管理资源。

**之前讨论要点**：
历史讨论中，参与者们对补丁的实现细节进行了深入探讨，尤其是如何在 KVM 中保持主机 MPAM 配置不变，以及如何处理 MPAMSM_EL1 寄存器的访问。部分补丁得到了测试和审核，显示出其在功能上的有效性。

**本周新讨论进展**：
本周的讨论中，Ben Horgan 和其他参与者对补丁进行了进一步的审查和修改建议。Marc Zyngier 对多个补丁表示认可，并提出了具体的修改意见。Punit Agrawal 报告了在 MPAM 支持的平台上进行测试的结果，确认了部分功能的正常工作，但也指出了一些未暴露的控制和监测功能。最后，Zeng Heng 提出了关于 CDP 启用时 RMID（资源监控 ID）提前释放的问题，寻求社区的反馈。

总体来看，本周的讨论集中在对补丁的细节审查和功能验证上，推动了 ARM MPAM 支持的进一步完善。

#### 📝 邮件列表

1. **[02-24 17:56]** [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[02-24 17:56]** [PATCH v5 02/41] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-24 17:56]** [PATCH v5 03/41] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-24 17:56]** [PATCH v5 11/41] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-24 17:56]** [PATCH v5 12/41] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-24 17:57]** [PATCH v5 31/41] arm_mpam: resctrl: Add resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[02-24 17:57]** [PATCH v5 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[03-01 09:28]** Re: [PATCH v5 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
9. **[03-02 17:11]** Re: [PATCH v5 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[03-02 17:52]** Re: [PATCH v5 02/41] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-02 17:54]** Re: [PATCH v5 03/41] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-02 17:58]** Re: [PATCH v5 11/41] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-02 18:15]** Re: [PATCH v5 12/41] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[03-03 16:33]** Re: [PATCH v5 12/41] KVM: arm64: Use kernel-space partid
 configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[03-03 20:18]** Re: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Punit Agrawal <punit.agrawal@oss.qualcomm.com>
16. **[03-04 09:42]** Re: [PATCH v5 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[03-07 17:29]** Re: [PATCH v5 31/41] arm_mpam: resctrl: Add resctrl_arch_rmid_read()
 and resctrl_arch_reset_rmid()
   - 发件人: Zeng Heng <zengheng4@huawei.com>

---

### Thread 8: [PATCH v1 00/13] KVM: arm64: Refactor user_mem_abort() into a
 state-object model

**📧 邮件数**: 16 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Mar 2026 14:02:19 +0000

#### 🤖 AI 总结

本邮件线程讨论了对 KVM（Kernel-based Virtual Machine）中 arm64 架构的 `user_mem_abort()` 函数进行重构的补丁系列。Fuad Tabba 提出了 13 个补丁，旨在将该函数重构为状态对象模型，以提高代码的可读性和可维护性。

历史讨论中，`user_mem_abort()` 函数因其复杂性和庞大体积导致了多次错误和内存泄漏问题。Fuad 指出，函数内部的清理逻辑难以追踪，导致了结构体引用泄漏和未初始化指针等问题。因此，重构的目标是将其拆分为多个小的、专注的辅助函数，以简化逻辑并减少错误。

本周的新讨论中，Fuad 提交了多个补丁，逐步实现了重构目标。主要进展包括：
1. 引入了 `struct kvm_s2_fault` 结构体来封装错误处理所需的状态信息。
2. 将 `user_mem_abort()` 中的逻辑分解为多个小函数，如 `kvm_s2_fault_pin_pfn()` 和 `kvm_s2_fault_map()`，以处理特定的任务。
3. 优化了代码逻辑，简化了变量的使用，消除了冗余的状态变量。

Marc Zyngier 对补丁表示认可，并提出进一步拆分和简化的建议，认为当前的状态对象结构过于复杂，建议将架构状态信息与其他上下文分开处理。Fuad 对此表示赞同，并愿意继续改进代码。

整体而言，本次讨论围绕着对 KVM 的重要功能进行重构，以提升代码质量和系统稳定性。

#### 📝 邮件列表

1. **[03-06 14:02]** [PATCH v1 00/13] KVM: arm64: Refactor user_mem_abort() into a
 state-object model
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-06 14:02]** [PATCH v1 01/13] KVM: arm64: Extract VMA size resolution in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[03-06 14:02]** [PATCH v1 02/13] KVM: arm64: Introduce struct kvm_s2_fault to user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[03-06 14:02]** [PATCH v1 03/13] KVM: arm64: Extract PFN resolution in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[03-06 14:02]** [PATCH v1 04/13] KVM: arm64: Isolate mmap_read_lock inside new
 kvm_s2_fault_get_vma_info() helper
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[03-06 14:02]** [PATCH v1 05/13] KVM: arm64: Extract stage-2 permission logic in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[03-06 14:02]** [PATCH v1 06/13] KVM: arm64: Extract page table mapping in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[03-06 14:02]** [PATCH v1 07/13] KVM: arm64: Simplify nested VMA shift calculation
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[03-06 14:02]** [PATCH v1 08/13] KVM: arm64: Remove redundant state variables from
 struct kvm_s2_fault
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[03-06 14:02]** [PATCH v1 09/13] KVM: arm64: Simplify return logic in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[03-06 14:02]** [PATCH v1 10/13] KVM: arm64: Initialize struct kvm_s2_fault
 completely at declaration
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[03-06 14:02]** [PATCH v1 11/13] KVM: arm64: Optimize early exit checks in kvm_s2_fault_pin_pfn()
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[03-06 14:02]** [PATCH v1 12/13] KVM: arm64: Hoist MTE validation check out of MMU
 lock path
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[03-06 14:02]** [PATCH v1 13/13] KVM: arm64: Clean up control flow in kvm_s2_fault_map()
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[03-06 15:34]** Re: [PATCH v1 00/13] KVM: arm64: Refactor user_mem_abort() into a state-object model
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[03-06 15:44]** Re: [PATCH v1 00/13] KVM: arm64: Refactor user_mem_abort() into a
 state-object model
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v12 06/46] arm64: RMI: Define the user ABI

**📧 邮件数**: 16 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 02 Mar 2026 14:25:37 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下 RMI（Realm Management Interface）用户 ABI（应用程序二进制接口）的定义，具体是针对 PSCI（Power State Coordination Interface）处理的补丁。

**原始补丁内容**：
补丁旨在定义 RMI 的用户 ABI，特别是如何处理 PSCI 调用，以便在虚拟机监控器（VMM）和用户空间之间进行有效的交互。

**之前讨论要点**：
在历史讨论中，参与者探讨了如何强制 VMM 处理 PSCI 调用的必要性，以及不同的 VCPU 之间如何协调 PSCI 调用的返回值和状态。Marc Zyngier 和 Steven Price 讨论了 RMM（Realm Management Monitor）在处理 PSCI 请求时的角色和复杂性，尤其是在 VCPU 运行时的状态一致性问题。

**本周的新讨论与进展**：
本周的讨论集中在如何确保 RMM 在处理 PSCI_CPU_ON 时的操作顺序。Marc Zyngier 提出，RMM 需要在 VCPU 运行之前了解 MPIDR（多处理器 ID）映射，以便正确处理 REC（Realm Execution Context）对象。Suzuki K Poulose 则认为，VMM 应该能够在目标 VCPU 开始运行时直接处理 PSCI 调用，而不需要额外的用户空间干预。Steven Price 表示希望简化这一过程，认为 RMM 不应过多依赖于用户空间的参与。整体来看，讨论围绕如何优化 RMI 的设计以提高效率和简化流程，特别是在处理 PSCI 调用时的复杂性。

#### 📝 邮件列表

1. **[03-02 14:25]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-02 14:40]** Re: [PATCH v12 11/46] arm64: RMI: Activate realm on first VCPU run
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-02 14:56]** Re: [PATCH v12 20/46] arm64: RMI: Allow populating initial contents
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-02 15:23]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
5. **[03-02 16:31]** Re: [PATCH v12 11/46] arm64: RMI: Activate realm on first VCPU run
   - 发件人: Steven Price <steven.price@arm.com>
6. **[03-02 16:39]** Re: [PATCH v12 27/46] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-02 16:46]** Re: [PATCH v12 20/46] arm64: RMI: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
8. **[03-02 17:13]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
9. **[03-03 09:26]** Re: [PATCH v12 27/46] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
10. **[03-03 13:04]** Re: [PATCH v12 27/46] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-03 13:11]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-03 13:13]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-03 14:23]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[03-03 14:37]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[03-03 16:02]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
16. **[03-04 12:08]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 10: [PATCH 0/4] arm64: Work around C1-Pro erratum 4193714 (CVE-2026-0995)

**📧 邮件数**: 15 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  2 Mar 2026 16:57:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm C1-Pro 处理器的一个已知缺陷（CVE-2026-0995），该缺陷导致在执行 TLB 无效化和 DSB 操作时，可能无法确保所有 SME 内存访问的完成。为了解决这一问题，提出了一系列补丁。

**原始补丁内容**：
补丁集包含四个部分，主要目的是通过在 TLB 无效化后在所有受影响的 CPU 上执行 DSB 来确保 SME 访问的完成。补丁 1 和 2 为后续补丁做准备，补丁 3 实现了针对内核的缺陷解决方案，补丁 4 处理了 pKVM 的情况，确保不会影响受保护的客户机安全。

**之前讨论要点**：
历史讨论中，参与者们关注如何有效地实施这一工作区，以避免对系统性能的影响，并确保安全性。补丁的设计考虑了不同的执行环境（如用户空间和内核空间），并讨论了如何在不同 CPU 上同步操作。

**本周的新讨论与进展**：
本周的讨论集中在补丁的具体实现细节和潜在问题上。参与者对补丁的命名、功能和实现方式提出了建议和修改意见，特别是关于如何处理 SME 访问的同步问题，以及在不同上下文中是否需要额外的检查。Catalin Marinas 和 Will Deacon 等人对补丁的有效性和潜在影响进行了深入探讨，并提出了进一步的优化建议。整体上，讨论表明对补丁的认可，但也强调了需要在实施前解决的细节问题。

#### 📝 邮件列表

1. **[03-02 16:57]** [PATCH 0/4] arm64: Work around C1-Pro erratum 4193714 (CVE-2026-0995)
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[03-02 16:57]** [PATCH 1/4] arm64: tlb: Use __tlbi_sync_s1ish_kernel() for kernel TLB maintenance
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[03-02 16:57]** [PATCH 2/4] arm64: tlb: Pass the corresponding mm to __tlbi_sync_s1ish()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[03-02 16:57]** [PATCH 3/4] arm64: errata: Work around early CME DVMSync acknowledgement
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[03-02 16:57]** [PATCH 4/4] KVM: arm64: Add SMC hook for SME dvmsync erratum
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[03-03 13:12]** Re: [PATCH 1/4] arm64: tlb: Use __tlbi_sync_s1ish_kernel() for
 kernel TLB maintenance
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[03-05 11:27]** Re: [PATCH 1/4] arm64: tlb: Use __tlbi_sync_s1ish_kernel() for
 kernel TLB maintenance
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
8. **[03-05 14:32]** Re: [PATCH 3/4] arm64: errata: Work around early CME DVMSync
 acknowledgement
   - 发件人: Will Deacon <will@kernel.org>
9. **[03-05 14:32]** Re: [PATCH 4/4] KVM: arm64: Add SMC hook for SME dvmsync erratum
   - 发件人: Will Deacon <will@kernel.org>
10. **[03-05 14:33]** Re: [PATCH 2/4] arm64: tlb: Pass the corresponding mm to
 __tlbi_sync_s1ish()
   - 发件人: Will Deacon <will@kernel.org>
11. **[03-05 19:19]** Re: [PATCH 2/4] arm64: tlb: Pass the corresponding mm to
 __tlbi_sync_s1ish()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[03-06 11:15]** Re: [PATCH 2/4] arm64: tlb: Pass the corresponding mm to
 __tlbi_sync_s1ish()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
13. **[03-06 12:00]** Re: [PATCH 3/4] arm64: errata: Work around early CME DVMSync
 acknowledgement
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
14. **[03-06 12:19]** Re: [PATCH 3/4] arm64: errata: Work around early CME DVMSync
 acknowledgement
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
15. **[03-06 12:52]** Re: [PATCH 4/4] KVM: arm64: Add SMC hook for SME dvmsync erratum
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 11: [PATCH v2 0/3] KVM: arm64: Fix SPE and TRBE nVHE world switch

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 27 Feb 2026 21:21:32 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在解决 nVHE（非虚拟化高效）世界切换时的 SPE（统计性能监控）和 TRBE（跟踪缓冲区单元）相关问题。

**原始补丁内容**：
补丁分为三个部分，主要目的是在运行于客人上下文时禁用 TRBE 和 SPE，以防止潜在的性能监控数据生成和跟踪数据的错误。补丁中增加了缺失的内存屏障，并对 TRBE 和 SPE 的已知 CPU 错误进行了处理。

**之前讨论要点**：
历史讨论中，Will Deacon 提出了补丁的初步版本，强调了修复的必要性和补丁的具体改动，包括内存屏障的添加和对已知问题的处理。补丁的目标是确保在虚拟化环境中，性能监控不会干扰到客人虚拟机的正常运行。

**本周的新讨论与进展**：
在本周的讨论中，参与者对补丁进行了审查和测试。Suzuki K Poulose 对 TRBE 和 SPE 的补丁表示认可，并提出了一些小的改进建议。Leo Yan 进行了实际测试，确认补丁在其硬件上运行良好，收集了 TRBE 跟踪数据。James Clark 也提出了与 PMU（性能监控单元）相关的补丁，修复了 PMU 版本字段的符号问题，并确保与性能监控相关的功能在 KVM 中的正确性。

整体来看，讨论围绕着确保 KVM 在 arm64 架构下的性能监控功能的稳定性和可靠性展开，补丁得到了积极的反馈和验证。

#### 📝 邮件列表

1. **[02-27 21:21]** [PATCH v2 0/3] KVM: arm64: Fix SPE and TRBE nVHE world switch
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-27 21:21]** [PATCH v2 1/3] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
3. **[02-27 21:21]** [PATCH v2 2/3] KVM: arm64: Disable SPE Profiling Buffer when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
4. **[03-03 09:23]** Re: [PATCH v2 1/3] KVM: arm64: Disable TRBE Trace Buffer Unit when
 running in guest context
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[03-03 09:48]** Re: [PATCH v2 2/3] KVM: arm64: Disable SPE Profiling Buffer when
 running in guest context
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[03-03 14:39]** Re: [PATCH v2 2/3] KVM: arm64: Disable SPE Profiling Buffer when
 running in guest context
   - 发件人: Will Deacon <will@kernel.org>
7. **[03-03 15:01]** Re: [PATCH v2 2/3] KVM: arm64: Disable SPE Profiling Buffer when
 running in guest context
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[03-03 17:39]** Re: [PATCH v2 1/3] KVM: arm64: Disable TRBE Trace Buffer Unit when
 running in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
9. **[03-05 16:28]** [PATCH v2 0/3] KVM: arm64: Read PMUVer as unsigned
   - 发件人: James Clark <james.clark@linaro.org>
10. **[03-05 16:28]** [PATCH v2 1/3] KVM: arm64: Read PMUVer as unsigned
   - 发件人: James Clark <james.clark@linaro.org>
11. **[03-05 16:28]** [PATCH v2 2/3] arm64: cpufeature: Make PMUVer and PerfMon unsigned
   - 发件人: James Clark <james.clark@linaro.org>
12. **[03-05 16:28]** [PATCH v2 3/3] arm64: cpufeature: Use pmuv3_implemented() function
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 12: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context

**📧 邮件数**: 12 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 16 Feb 2026 14:29:31 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中，当运行在客户机上下文时禁用 TRBE（Trace Buffer Unit）的问题。原始的 patch 提出在客户机模式下禁用 TRBE，以避免其在架构原则上的不一致性和潜在的错误。

在历史讨论中，参与者们探讨了 TRBE 的缺陷及其对系统稳定性的影响，特别是与其他特性（如 SPE 和 ETE）之间的关系。Marc Zyngier 和 Will Deacon 等人指出，TRBE 在上下文切换时可能会引发问题，并讨论了相关的 erratum（错误报告），如 #2064142 和 #2038923，强调了在切换时需要清除特定寄存器以避免状态不一致。

在本周的新讨论中，Leo Yan 和 Suzuki K Poulose 进一步澄清了 TRFCR 寄存器与 TRBE 的关系，确认 TRFCR 是由 FEAT_TRF 引入的，与 TRBE 是不同的功能。Leo 提出将始终保存和恢复 TRBE 状态，以防止在 CPU 进入空闲状态后寄存器处于不确定状态。此外，讨论中提到在合并当前补丁系列后，可能会考虑将其回溯到早期版本。

总的来说，邮件讨论集中在如何确保 TRBE 在客户机上下文中安全禁用，以及如何处理相关寄存器的状态，以提高系统的稳定性和可靠性。

#### 📝 邮件列表

1. **[02-16 14:29]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-16 15:05]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
3. **[02-16 18:14]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-17 14:19]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
5. **[02-17 14:52]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
6. **[02-17 19:01]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
7. **[02-19 13:54]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
8. **[02-19 18:58]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
9. **[02-25 12:09]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
10. **[02-27 18:07]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
11. **[03-03 10:36]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
12. **[03-03 10:47]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 13: [PATCH v3 0/5] Support the FEAT_HDBSS introduced in Armv9.5

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Feb 2026 12:04:16 +0800

#### 🤖 AI 总结

本邮件线程讨论了对 ARMv9.5 引入的硬件脏页状态跟踪结构（HDBSS）特性的支持，主要涉及一系列补丁的实现和优化。

**原始补丁内容**：
补丁系列旨在支持 HDBSS 特性，该特性通过硬件辅助来跟踪翻译表描述符的脏状态，显著减少脏页扫描的开销。HDBSS 在虚拟化环境中通过用户空间的 ioctl 接口启用，主要在 VHE 模式下工作。

**之前讨论要点**：
在历史讨论中，参与者提出了将 HDBSS 自动启用的建议，以简化用户空间的操作，避免每次写入后都需要处理故障。此外，关于如何在迁移过程中分配缓冲区的讨论也引发了共识，认为在迁移的第一步中启用 HDBSS 是合理的。

**本周新讨论进展**：
本周的讨论集中在补丁的细节和实现优化上。参与者确认了在分配页面时的对齐性问题，并讨论了如何在 vcpu_put 和 guest exit 之间合理安排 HDBSS 的刷新操作，以避免不必要的性能开销。最终，大家达成一致，计划在特定事件触发时刷新 HDBSS 缓冲区，而不是在每次客体退出时刷新，从而提高效率。参与者还计划在下一版本中测试 HDBSS 在脏环模式下的表现。

#### 📝 邮件列表

1. **[02-25 12:04]** [PATCH v3 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
2. **[02-25 12:04]** [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
3. **[02-25 17:46]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>
4. **[02-27 18:47]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
5. **[02-27 14:10]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>
6. **[03-04 11:06]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
7. **[03-04 12:08]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>
8. **[03-04 15:40]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>
9. **[03-05 15:37]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
10. **[03-06 17:27]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Tian Zheng <zhengtian10@huawei.com>
11. **[03-06 15:01]** Re: [PATCH v3 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF events
   - 发件人: Leonardo Bras <leo.bras@arm.com>

---

### Thread 14: [PATCH v1 0/2] KVM: arm64: Fix a couple of latent bugs in user_mem_abort()

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  4 Mar 2026 16:22:20 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 `user_mem_abort()` 函数的两个潜在错误进行修复，包含两个补丁（patch）。

**原始补丁内容**：
第一个补丁解决了在处理原子操作时，因早期返回而导致的页面引用泄漏问题。第二个补丁则修复了在处理嵌套阶段2故障时，`vma_shift` 变量未更新的问题，可能导致错误的边界信息发送给用户空间。

**之前讨论要点**：
在历史讨论中，Fuad Tabba 提到这些问题的存在表明 `user_mem_abort()` 函数的复杂性和脆弱性，强调了需要进行重构以简化状态流。之前的讨论中提到，类似的页面泄漏问题已在早期修复，但由于新引入的错误处理路径，问题再次出现。

**本周新讨论及进展**：
本周的讨论中，Fuad 提交了两个补丁，并得到了参与者的积极反馈。Yao Yuan 对第一个补丁进行了审核，表示支持。Marc Zyngier 提出了对第二个补丁的简化建议，Fuad 表示会在本地进行修正。最终，两个补丁均已被应用到修复分支中，标志着问题的解决。

总的来说，本周的讨论集中在修复 KVM 中的具体问题，并为未来的重构工作奠定了基础。

#### 📝 邮件列表

1. **[03-04 16:22]** [PATCH v1 0/2] KVM: arm64: Fix a couple of latent bugs in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-04 16:22]** [PATCH v1 1/2] KVM: arm64: Fix page leak in user_mem_abort() on
 atomic fault
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[03-04 16:22]** [PATCH v1 2/2] KVM: arm64: Fix vma_shift staleness on nested hwpoison path
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[03-05 09:57]** Re: [PATCH v1 1/2] KVM: arm64: Fix page leak in user_mem_abort() on
 atomic fault
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
5. **[03-05 16:07]** Re: [PATCH v1 2/2] KVM: arm64: Fix vma_shift staleness on nested hwpoison path
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-05 16:13]** Re: [PATCH v1 2/2] KVM: arm64: Fix vma_shift staleness on nested
 hwpoison path
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[03-05 16:22]** Re: [PATCH v1 2/2] KVM: arm64: Fix vma_shift staleness on nested hwpoison path
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[03-05 16:51]** Re: [PATCH v1 0/2] KVM: arm64: Fix a couple of latent bugs in user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[03-05 16:55]** Re: [PATCH v1 0/2] KVM: arm64: Fix a couple of latent bugs in user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[03-06 10:48]** Re: [PATCH v1 0/2] KVM: arm64: Fix a couple of latent bugs in user_mem_abort()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled()
 checks from hypercalls

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 3 Mar 2026 15:45:16 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是移除 hypercalls 中对 `is_protected_kvm_enabled()` 的检查。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的目的是简化 hypercall 的实现，特别是在 pKVM（保护 KVM）启用的情况下，确保 hypercall 的可用性和安全性。

本周的新讨论中，参与者 Will Deacon 和 Alexandru Elisei 对补丁进行了深入的技术交流。Will 提出了保留注释的建议，以便更清晰地界定 hypercalls 的块，并讨论了如何在处理 hypercall 时确保指针参数的安全性。他强调，补丁系列的重点是处理来宾内存，后续将进一步加强 vCPU/VM 结构的安全性。Alexandru 对补丁的修改表示认可，并感谢 Will 的解释。

总体来看，本周的讨论集中在补丁的细节和实现逻辑上，参与者们对补丁的方向表示支持，并在技术细节上进行了有效的沟通和澄清。

#### 📝 邮件列表

1. **[03-03 15:45]** Re: [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled()
 checks from hypercalls
   - 发件人: Will Deacon <will@kernel.org>
2. **[03-04 14:06]** Re: [PATCH v2 25/35] KVM: arm64: Reclaim faulting page from pKVM in
 spurious fault handler
   - 发件人: Will Deacon <will@kernel.org>
3. **[03-04 14:06]** Re: [PATCH v2 14/35] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
4. **[03-04 14:08]** Re: [PATCH v2 24/35] KVM: arm64: Introduce hypercall to force
 reclaim of a protected page
   - 发件人: Will Deacon <will@kernel.org>
5. **[03-06 11:33]** Re: [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled()
 checks from hypercalls
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[03-06 11:34]** Re: [PATCH v2 14/35] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 16: [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 20 Feb 2026 00:42:13 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测试代码中类型的更新，主要是将一些数据类型重命名为与内核中使用的类型更一致。原始的补丁（patch）由 David Matlack 提出，内容包括将 `vm_vaddr_t` 和 `vm_paddr_t` 分别重命名为 `gva_t` 和 `gpa_t`，并将标准的整数类型如 `uint64_t` 替换为更简洁的 `u64` 等。这一系列改动旨在使 KVM 自测试代码更加简洁，并与内核代码保持一致。

在历史讨论中，David Matlack 详细说明了补丁的目的和实现方法，并提到在补丁中包含了必要的头文件以避免编译错误。

在本周的新讨论中，Sean Christopherson 对补丁提出了一些建议，包括将某个函数转换为 `pread_u64()`。他还提到由于时间原因，未能及时将补丁合并到 `kvm/next` 分支，但计划在下一个合并窗口期间准备一个新的版本（v3）并向 Paolo 提交请求。David Matlack 对此表示赞同，并感谢 Sean 的建议。

总体来看，本周的讨论主要集中在补丁的后续处理和进一步的改进建议上。

#### 📝 邮件列表

1. **[02-20 00:42]** [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types
   - 发件人: David Matlack <dmatlack@google.com>
2. **[02-20 00:42]** [PATCH v2 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: David Matlack <dmatlack@google.com>
3. **[03-05 09:19]** Re: [PATCH v2 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[03-05 09:22]** Re: [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[03-05 09:26]** Re: [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types
   - 发件人: David Matlack <dmatlack@google.com>
6. **[03-05 09:26]** Re: [PATCH v2 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: David Matlack <dmatlack@google.com>

---

### Thread 17: [PATCH] arm64: Implement clear_pages()

**📧 邮件数**: 6 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 03 Mar 2026 11:06:13 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 arm64 架构实现 `clear_pages()` 函数的补丁。该补丁旨在优化现有的 `clear_page()` 函数，使其能够一次性清除多个页面，从而提高性能。具体实现上，`clear_page()` 被定义为 `clear_pages()` 的静态内联特例，后者计算所需清除的总字节数并调用汇编例程 `clear_pages_asm`。

在之前的讨论中，参与者们关注了该补丁的性能提升，尤其是在 QEMU 和实际硬件上的表现。Linus Walleij 提到，补丁在 QEMU 中的性能提升有限，可能与实际硬件的表现不一致。同时，Will Deacon 和 Catalin Marinas 提出，考虑将更多代码移回 C 语言，以便编译器进行更好的优化。

本周的新讨论中，Linus Walleij 进一步分析了补丁的实现细节，指出通过将多页清除操作合并为一次性计算，可以减少循环的开销。Ankur Arora 也提到，清除操作的预empt模型可能影响性能，建议在特定条件下进行调度。总体而言，参与者们对该补丁的实现和潜在的性能影响进行了深入探讨，尚未达成最终结论。

#### 📝 邮件列表

1. **[03-03 11:06]** [PATCH] arm64: Implement clear_pages()
   - 发件人: Linus Walleij <linusw@kernel.org>
2. **[03-03 14:46]** Re: [PATCH] arm64: Implement clear_pages()
   - 发件人: Will Deacon <will@kernel.org>
3. **[03-03 15:45]** Re: [PATCH] arm64: Implement clear_pages()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[03-04 01:39]** Re: [PATCH] arm64: Implement clear_pages()
   - 发件人: Linus Walleij <linusw@kernel.org>
5. **[03-04 00:05]** Re: [PATCH] arm64: Implement clear_pages()
   - 发件人: Ankur Arora <ankur.a.arora@oracle.com>
6. **[03-04 08:49]** Re: [PATCH] arm64: Implement clear_pages()
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 18: [PATCH v12 00/30] Tracefs support for pKVM

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 19 Feb 2026 15:02:37 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁（PATCH v12 00/30）。该补丁旨在为保护模式下的虚拟化提供调试和分析工具，Tracefs 被认为是一个理想的选择，因为它易于使用且支持多种工具。

在历史讨论中，Vincent Donnefort 提出了该补丁的背景，强调了 Tracefs 的优势，包括其简单性和与内核及虚拟机之间的良好兼容性。Steven Rostedt 提到在补丁系列与当前的追踪树之间可能会出现重大冲突，并计划在 -rc2 发布后直接将补丁应用到他的树上，以便在下一个合并窗口中进行整合。Marc Zyngier 也表示支持这一方案，并要求在 -rc2 发布后提供链接以便处理。

在本周的新讨论中，Steven Rostedt 指出与 v7.0-rc2 存在一些小冲突，要求 Vincent 进行重新基于并重新提交补丁。Vincent 随后回应表示将于次日发送一个重新基于的新版本。这表明该补丁仍在积极推进中，尽管面临一些技术挑战。

#### 📝 邮件列表

1. **[02-19 15:02]** [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-19 13:02]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
3. **[02-19 19:11]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-05 11:17]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
5. **[03-05 18:35]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 19: [PATCH] KVM: arm64: Skip interrupts in LRs during EOIcount replay

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  7 Mar 2026 12:59:50 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 ARM64 架构下处理中断的一个补丁，主要针对在 EOIcount 重放过程中跳过 LRs（中断处理寄存器）中的中断。

**原始补丁内容**：
补丁旨在解决在 EOIcount 重放时，如果当前中断仍在 LR 中，可能导致错误的中断去激活，进而引发中断风暴和启动失败的问题。补丁通过在重放过程中跳过当前分配给 LR 的中断来解决这一问题，从而确保 Android 虚拟机能够正常启动。

**之前讨论要点**：
在之前的讨论中，Valentine Burley 提出了补丁的背景，指出在处理过程中，可能会选择到一个仍在 LR 中的中断，导致不必要的去激活。Marc Zyngier 也参与了讨论，指出在某些情况下，可能会出现竞争条件，从而影响中断处理的正确性。

**本周的新讨论与进展**：
本周的讨论中，Valentine 对补丁进行了测试，确认其在 SC7180 Trogdor 设置下完全解决了问题，使 Cuttlefish 虚拟机能够可靠启动。Marc 也对补丁进行了小幅调整，建议将重启指针的存储方式从每个虚拟 CPU 改为每个 CPU，以提高效率。最终，Marc 表示将正式发布更新后的补丁供确认。

总体来看，本周的讨论集中在补丁的有效性和小幅优化上，参与者们对解决方案表示满意。

#### 📝 邮件列表

1. **[03-07 12:59]** [PATCH] KVM: arm64: Skip interrupts in LRs during EOIcount replay
   - 发件人: Valentine Burley <valentine.burley@collabora.com>
2. **[03-07 16:33]** Re: [PATCH] KVM: arm64: Skip interrupts in LRs during EOIcount replay
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-07 19:29]** Re: [PATCH] KVM: arm64: Skip interrupts in LRs during EOIcount
 replay
   - 发件人: Valentine Burley <valentine.burley@collabora.com>
4. **[03-07 19:10]** Re: [PATCH] KVM: arm64: Skip interrupts in LRs during EOIcount replay
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 04 Mar 2026 18:55:04 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: 在主机阶段2故障期间正确调整范围”，主要讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁。

1. **原始 patch/问题的内容**：该补丁旨在解决在主机阶段2故障时范围调整不当的问题，特别是处理内存映射时可能出现的错误。

2. **之前的讨论要点**：在历史讨论中，未提供具体的背景信息，但可以推测该补丁是为了修复在特定情况下（例如在保护模式下）引发的启动问题。

3. **本周的新讨论、进展或结论**：本周的讨论主要集中在补丁引发的问题上。Marc Zyngier 提到该补丁导致 O6 板无法启动，并通过回退补丁解决了问题。他还指出，内存块表的结构可能导致对某些地址的访问失败。Quentin Perret 认为在最后一级映射时，应确保页面对齐，以避免映射邻近的私有区域。最后，Quentin 表示他已经准备好新的补丁，并希望得到反馈后再发布。

总体来看，本周的讨论强调了补丁在实际应用中的问题，并提出了进一步的修复建议。

#### 📝 邮件列表

1. **[03-04 18:55]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-05 10:55]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-05 13:13]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2
 faults
   - 发件人: Quentin Perret <qperret@google.com>
4. **[03-05 13:22]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH RESEND 0/2] KVM: arm64: nv: Expose shadow page tables in debugfs

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Sun,  8 Mar 2026 23:18:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要目的是在 debugfs 中暴露影子页表，以提高嵌套虚拟化（NV）的调试和测试能力。

**原始补丁/问题内容**：
补丁系列的核心是将影子页表暴露在 debugfs 中，补丁包括对 KVM 页表转储代码的修改，使其能够处理不同的 S2 MMU（内存管理单元）。补丁文件的命名格式为 `0x<vttbr>-0x<vtcr>-s2-{en,dis}abled`，用于标识 S2 MMU 的状态。

**之前讨论要点**：
在历史讨论中，虽然没有具体的邮件记录，但可以推测补丁的提出是为了应对嵌套虚拟化的调试需求，尤其是在处理不同 MMU 状态时的可读性和可测试性。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的重新提交上，Wei-Lin Chang 提到之前的提交中包含了错误的提交信息，并进行了修正。补丁的实现细节包括在每个 VM 创建时为其创建一个名为 "nested" 的目录，并在其中暴露有效的 S2 MMU 的影子页表。补丁的创建和删除与 S2 MMU 的有效性变化相对应。此外，补丁的实现依赖于 `CONFIG_PTDUMP_STAGE2_DEBUGFS` 配置选项。参与者欢迎对文件命名的建议，并表示愿意修改过于冗长的变量和函数名称。

#### 📝 邮件列表

1. **[03-08 23:18]** [PATCH RESEND 0/2] KVM: arm64: nv: Expose shadow page tables in debugfs
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>
2. **[03-08 23:18]** [PATCH RESEND 1/2] KVM: arm64: ptdump: Make KVM ptdump code s2 mmu aware
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>
3. **[03-08 23:18]** [PATCH RESEND 2/2] KVM: arm64: nv: Expose shadow page tables in debugfs
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>

---

### Thread 22: [PATCH 0/2] KVM: arm64: nv: Expose shadow page tables in debugfs

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Sun,  8 Mar 2026 22:56:59 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是在 debugfs 中暴露影子页表，以提高调试和测试的能力。

**原始补丁内容**：
补丁系列包括两个部分：第一部分是将 KVM 的 ptdump 代码修改为支持不同的 s2 MMU（内存管理单元），以便后续能够导出影子页表；第二部分则是实际实现了在 debugfs 中暴露影子页表的功能，创建了一个名为 "nested" 的目录，里面包含每个有效 s2 MMU 的影子页表。

**之前讨论要点**：
在历史讨论中，参与者对如何格式化影子页表的文件名进行了探讨，当前的命名方式为 "0x<vttbr>-0x<vtcr>-s2-{en,dis}abled"，虽然直观但不够清晰。参与者也欢迎对命名方式提出改进建议。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的具体实现上。Wei-Lin Chang 提出了补丁的详细代码修改，包括在 KVM 的 ptdump 代码中引入 s2 MMU 的支持，以及在 debugfs 中创建和删除影子页表文件的逻辑。此外，补丁还通过 CONFIG_PTDUMP_STAGE2_DEBUGFS 进行配置控制。参与者对补丁的实现表示认可，并期待进一步的反馈和建议。

#### 📝 邮件列表

1. **[03-08 22:56]** [PATCH 0/2] KVM: arm64: nv: Expose shadow page tables in debugfs
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>
2. **[03-08 22:57]** [PATCH 1/2] KVM: arm64: ptdump: Make KVM ptdump code s2 mmu aware
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>
3. **[03-08 22:57]** [PATCH 2/2] KVM: arm64: nv: Expose shadow page tables in debugfs
   - 发件人: Wei-Lin Chang <weilin.chang@arm.com>

---

### Thread 23: [PATCH] KVM: arm64: vgic: Pick EOIcount deactivations from AP-list tail

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  7 Mar 2026 19:11:51 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VGIC（虚拟通用中断控制器）处理中的一个补丁，旨在解决虚拟机在启动时因中断处理不当而导致的问题。

原始补丁的内容是修复在处理 EOI（结束中断）计数时，从 AP 列表中错误地选择中断的顺序。具体来说，当维护中断处理较慢时，可能会从 LRs（中断链接寄存器）中激活额外的中断，导致错误的中断被停用。补丁通过跟踪最后一个进入 LRs 的中断，并在此之后进行 EOIcount 的停用处理，从而解决了这一问题。

在之前的讨论中，Valentine Burley 报告了虚拟机启动失败和中断丢失的问题，并提供了初步的补丁建议。Marc Zyngier 在补丁中感谢了 Valentine 的调查工作，并指出了问题的根源。

在本周的新讨论中，Valentine 对补丁进行了测试并确认修复有效。Marc Zyngier 随后表示已将该补丁应用于修复列表，并感谢参与者的贡献。这表明该补丁已成功解决了报告的问题，并得到了社区的认可。

#### 📝 邮件列表

1. **[03-07 19:11]** [PATCH] KVM: arm64: vgic: Pick EOIcount deactivations from AP-list tail
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-07 21:56]** Re:[PATCH] KVM: arm64: vgic: Pick EOIcount deactivations from
 AP-list tail
   - 发件人: Valentine Burley <valentine.burley@collabora.com>
3. **[03-07 21:49]** Re: [PATCH] KVM: arm64: vgic: Pick EOIcount deactivations from AP-list tail
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH] KVM: arm64: pkvm: Fallback to level-3 mapping on host stage-2 fault

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  5 Mar 2026 13:27:51 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: pkvm: Fallback to level-3 mapping on host stage-2 fault”，主要讨论了在 KVM（Kernel-based Virtual Machine）环境下处理 ARM64 架构的主机阶段2故障时的映射策略。

原始 patch 提出的内容是，当在某些情况下无法创建完全包含在内存块区域中的映射时，系统会失败并返回到故障指令。特别是在处理小于页面大小或不对齐的区域时，系统将回退到使用页面大小的映射，以确保不会出现更低的映射级别。

在之前的讨论中，Marc Zyngier 提到此问题的背景，指出在某些硬件（如 O6 板）上，系统无法以受保护模式启动，导致映射失败。

本周的新讨论中，Marc Zyngier 提交了该 patch，并得到了参与者 Quentin Perret 的审核确认。Quentin 表示已审核通过，随后 Marc 也确认该 patch 已应用于修复列表，标记为 commit: 8531d5a83d8eb8affb5c0249b466c28d94192603。这表明该问题得到了及时的解决和处理。

#### 📝 邮件列表

1. **[03-05 13:27]** [PATCH] KVM: arm64: pkvm: Fallback to level-3 mapping on host stage-2 fault
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-05 14:20]** Re: [PATCH] KVM: arm64: pkvm: Fallback to level-3 mapping on host
 stage-2 fault
   - 发件人: Quentin Perret <qperret@google.com>
3. **[03-05 15:20]** Re: [PATCH] KVM: arm64: pkvm: Fallback to level-3 mapping on host stage-2 fault
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 25: [PATCH] KVM: arm64: Read PMUVer as unsigned

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 05 Mar 2026 11:50:01 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中如何正确读取 PMUVer（性能监控单元版本）的问题。原始的 patch 提出了将 PMUVer 作为无符号字段读取，以解决在 Armv8.8 及更高版本中，因负值导致的 host_data_ptr(nr_event_counters) 初始化错误的问题。

在之前的讨论中，James Clark 提出了这个 patch，并指出现有实现中对 PMUVer 的处理不当，可能导致错误的事件计数器初始化。该 patch 的修复方法是使用无符号字段读取 PMUVer，从而避免负值问题。

本周的讨论中，Marc Zyngier 提出了一个问题，询问该 patch 在广告非架构化 PMU 的系统上如何工作。James Clark 随后回应，承认当前的实现可能无法处理这种情况，并提到已有的 pmuv3_implemented() 和 has_pmuv3() 函数可以复用，以简化代码并提高可读性。整体来看，本周的讨论集中在如何进一步改进和优化该 patch 的实现上。

#### 📝 邮件列表

1. **[03-05 11:50]** [PATCH] KVM: arm64: Read PMUVer as unsigned
   - 发件人: James Clark <james.clark@linaro.org>
2. **[03-05 11:59]** Re: [PATCH] KVM: arm64: Read PMUVer as unsigned
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-05 13:10]** Re: [PATCH] KVM: arm64: Read PMUVer as unsigned
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 26: [PATCH V2 0/2] arm64/mm: Drop TTBR_CNP_BIT and TTBR_ASID_MASK

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Mon,  2 Mar 2026 06:44:35 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构中的内存管理，具体涉及到去除 TTBR_CNP_BIT 和 TTBR_ASID_MASK 这两个自定义宏，直接使用现有的工具系统寄存器格式字段宏 TTBRx_EL1_CNP_BIT 和 TTBRx_EL1_ASID_MASK。

在历史讨论中，虽然没有具体的邮件记录，但可以推测此前已经有人提出了这一改动的建议，目的是为了简化代码并消除冗余。

本周的新讨论中，Anshuman Khandual 提出了两个补丁（PATCH V2 0/2），主要内容包括：
1. **补丁 1**：将所有 TTBR_ASID_MASK 宏实例替换为标准字段 TTBRx_EL1_ASID_MASK，并移除冗余的 TTBR_ASID_MASK 宏，确保功能不变。
2. **补丁 2**：将所有 TTBR_CNP_BIT 宏实例替换为 TTBRx_EL1_CnP，并同样移除冗余的 TTBR_CNP_BIT 宏，确保功能不变。

补丁的修改涉及多个文件，主要集中在 ARM64 架构的内存管理相关代码中。此次讨论的进展表明，开发者们正在积极推动代码的清理和优化，以提高代码的可维护性和一致性。

#### 📝 邮件列表

1. **[03-02 06:44]** [PATCH V2 0/2] arm64/mm: Drop TTBR_CNP_BIT and TTBR_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[03-02 06:44]** [PATCH V2 1/2] arm64/mm: Directly use TTBRx_EL1_ASID_MASK
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[03-02 06:44]** [PATCH V2 2/2] arm64/mm: Directly use TTBRx_EL1_CnP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 27: [PATCH] KVM: arm64: Remove the redundant ISB in __kvm_at_s1e2()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Mar 2026 15:44:22 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是移除函数 `__kvm_at_s1e2()` 中冗余的 ISB（Instruction Synchronization Barrier）指令。

在历史讨论中，未有相关的补充信息，直接进入本周的新讨论。Zenghui Yu 提出了补丁，指出在 `__kvm_at()` 函数中已经存在一个 ISB 指令，确保地址转换结果对后续的 PAR_EL1 读取可见，因此在 `__kvm_at_s1e2()` 中的冗余 ISB 指令可以被移除。补丁的具体修改是在 `arch/arm64/kvm/at.c` 文件中删除了两行与 ISB 相关的代码。

本周的第二封邮件中，Marc Zyngier 对该补丁表示感谢，并确认已将其应用于修复补丁中，标记为提交 ID 3599c714c08c324f0fcfa392bfb857c92c575400。这表明补丁得到了认可并已被合并。整体来看，本次讨论集中在优化代码、提高性能方面，成功移除了不必要的指令。

#### 📝 邮件列表

1. **[03-06 15:44]** [PATCH] KVM: arm64: Remove the redundant ISB in __kvm_at_s1e2()
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[03-06 10:48]** Re: [PATCH] KVM: arm64: Remove the redundant ISB in __kvm_at_s1e2()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 28: [PATCH 0/3] KVM: arm64: minor fixes about S2 page table walker

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Feb 2026 01:35:12 +0800

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 S2 页表遍历器的几个小修复。历史讨论中，Zenghui Yu 提出了一个补丁系列，共包含三项修复，目的是解决之前讨论中提到的一些问题，包括检查 S2 限制、报告地址大小故障以及在读取描述符失败时注入 SEA（系统错误中断）。

在本周的新讨论中，Marc Zyngier 确认了这些补丁已被应用于修复集，并列出了每个补丁的提交信息。这表明这些修复已经获得认可并成功整合到代码库中，进一步推动了 KVM 在 arm64 平台上的稳定性和可靠性。

总体而言，本周的进展显示出对之前讨论问题的积极响应，补丁的应用标志着向解决相关问题迈出了重要一步。

#### 📝 邮件列表

1. **[02-26 01:35]** [PATCH 0/3] KVM: arm64: minor fixes about S2 page table walker
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[03-06 10:48]** Re: [PATCH 0/3] KVM: arm64: minor fixes about S2 page table walker
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 29: [PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 28 Feb 2026 16:45:59 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation”，主要讨论了在 KVM 的 ARM64 架构中，如何在创建 VGIC 时提前初始化 VGIC 的分发器和重新分发器。

在历史讨论中，Marc Zyngier 提出了一个补丁，指出在调用 `vgic_allocate_private_irqs_locked()` 失败时，`kvm_vgic_create()` 函数会提前退出，导致 `dist->rd_regions` 未初始化。这会在后续的 `kvm_vgic_dist_destroy()` 函数中引发问题，因为它会尝试释放未初始化的资源。为了解决这个问题，Marc 提议将所有静态初始化提前，并确保在失败时能够合理地进行清理，同时在失败时重置 VGIC 模型。

在本周的新讨论中，Marc Zyngier 回复表示该补丁已被应用于修复分支，并感谢相关人员的贡献。补丁的提交 ID 为 `ac6769c8f948dff33265c50e524aebf9aa6f1be0`。

总结来看，本次讨论围绕 VGIC 初始化的安全性和稳定性展开，补丁的应用将有助于提升 KVM 的可靠性。

#### 📝 邮件列表

1. **[02-28 16:45]** [PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-05 15:19]** Re: [PATCH] KVM: arm64: Eagerly init vgic dist/redist on vgic creation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 30: [PATCH v9 00/30] KVM: arm64: Implement support for SME

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 6 Mar 2026 17:08:46 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现对 SME（Scalable Matrix Extension）的支持的补丁（PATCH v9 00/30）。该补丁旨在增强虚拟化层对新硬件特性的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是为了应对 ARM 架构中引入的新的扩展功能，以便更好地支持虚拟机监控程序（VMM）在处理这些新特性时的需求。

在本周的新讨论中，参与者 Mark Brown 对补丁进行了初步评估。他表示在查看该补丁后，认为其实现并不简单，特别是由于寄存器的热插拔特性可能会给 VMM 带来挑战。他提到，当前的 ABI（应用二进制接口）可能不适合简单的 VMM 实现，因此决定暂时不进行修改，并表示将会再次审视该补丁，以寻找更好的解决方案。

总体来看，本周的讨论强调了补丁在实际应用中的复杂性，并指出了未来可能需要进一步探讨的方向。

#### 📝 邮件列表

1. **[03-06 17:08]** Re: [PATCH v9 00/30] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 31: [PATCH] arm64: clear_page[s] using memset

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 06 Mar 2026 09:57:50 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构中使用 `memset` 函数来清除内存页面的补丁（patch）。Linus Walleij 提出了一个补丁，建议在清除内存时直接调用 `memset()`，而不是尝试预测编译器的行为。他指出，`memset()` 已经具备架构本地的 MOPS 优化，因此不需要额外的操作来保持这种优化。同时，他还实现了一个简化的接口，允许直接调用新的 `clear_pages()` 原型，以处理更大的页面块。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出此补丁的提出是基于对现有清除页面方法的性能和可读性考虑。

本周的新讨论中，Linus Walleij 提交了补丁，详细说明了修改内容，包括删除了原有的 `clear_page.S` 文件，并在相关文件中添加了对 `memset` 的引用。经过基准测试，未发现性能回归，结果差异在可接受的噪声范围内。这一补丁的提出旨在简化代码并提高可维护性。

#### 📝 邮件列表

1. **[03-06 09:57]** [PATCH] arm64: clear_page[s] using memset
   - 发件人: Linus Walleij <linusw@kernel.org>

---

### Thread 32: [PATCH v6 16/19] KVM: arm64: Add vCPU device attr to partition
 the PMU

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 5 Mar 2026 10:16:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中为虚拟 CPU（vCPU）设备添加 PMU（性能监控单元）属性的补丁（PATCH v6 16/19）。该补丁旨在增强虚拟化性能监控功能。

在历史讨论中，尚未提供相关背景信息，因此我们无法了解该补丁的详细历史讨论内容。

本周的讨论中，参与者 James Clark 针对补丁提出了一个拼写错误的指正，并询问为何不默认使用来宾分区，而是通过一个标志来控制是否回退到未传递的 PMU。他认为，如果在主机上已经创建了分区，那么来宾使用该分区的可能性很高，且这样做的开销更低，因此应该简化设置过程。此外，他还提到是否可以通过动态方法来避免在主机上设置标志的问题。

总体来看，本周的讨论集中在补丁的设计选择和使用便捷性上，提出了对当前实现方式的质疑和改进建议。

#### 📝 邮件列表

1. **[03-05 10:16]** Re: [PATCH v6 16/19] KVM: arm64: Add vCPU device attr to partition
 the PMU
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 33: [PATCH] KVM: arm64: Move inside all remaining TCR_XXX macros

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon,  2 Mar 2026 08:16:46 +0000

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 KVM（内核虚拟机）的补丁，旨在将所有剩余的 TCR_XXX 宏移入 KVM 特定的头文件 kvm_arm.h 中，以便在 KVM 中继续使用这些宏，因为不再存在 stage-1 的使用场景。

在历史讨论中，未提及任何具体的补丁或问题，因此本周的讨论是该补丁的首次提出。补丁的主要内容是将 TCR_XXX 宏从 pgtable-hwdef.h 文件中删除，并在 kvm_arm.h 文件中重新定义。这一改动涉及到 45 行代码的插入和删除，旨在清理代码并优化 KVM 的实现。

本周的新讨论由 Anshuman Khandual 提出，补丁已提交并适用于 v7.0-rc2 版本。邮件中还抄送了多位相关领域的专家，显示出对该补丁的重视和潜在的后续讨论。整体来看，此补丁的提出标志着 KVM 对 ARM64 架构的进一步优化，推动了内核虚拟化的进展。

#### 📝 邮件列表

1. **[03-02 08:16]** [PATCH] KVM: arm64: Move inside all remaining TCR_XXX macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request
 in kvm_vgic_destroy

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 28 Feb 2026 03:46:20 -0800

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理虚拟中断控制器（VGIC）时出现的内核分页请求错误。最初的补丁（patch）由 syzbot 提出，指出在执行 `kvm_vgic_destroy` 函数时发生了错误，导致内核无法处理分页请求。该问题的根源在于 `vgic_allocate_private_irqs_locked()` 函数的失败，导致在 `kvm_vgic_create()` 函数中未能正确初始化 `dist->rd_regions`，从而在后续的 `kvm_vgic_dist_destroy()` 中引发了错误。

在历史讨论中，Marc Zyngier 提到该问题与故障注入（fault injection）有关，认为这种方法可能导致更多的错误出现。Dmitry Vyukov 在本周的新讨论中回应了 Marc 的观点，指出 reproducer（重现程序）在开始时应该明确打印出故障注入设置失败的消息，以便用户了解可能的失败原因。Marc 也同意了这一点，并建议如果前提条件未满足，最好直接停止测试，因为这样不会产生有用的结果。

本周的讨论主要集中在如何改进故障注入的反馈机制，以提高测试的有效性和可用性。

#### 📝 邮件列表

1. **[02-28 03:46]** [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request
 in kvm_vgic_destroy
   - 发件人: syzbot <syzbot+f6a46b038fc243ac0175@syzkaller.appspotmail.com>
2. **[02-28 14:55]** Re: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request in kvm_vgic_destroy
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-02 13:59]** Re: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging
 request in kvm_vgic_destroy
   - 发件人: Dmitry Vyukov <dvyukov@google.com>
4. **[03-02 13:26]** Re: [syzbot] [kvmarm?] [kvm?] BUG: unable to handle kernel paging request in kvm_vgic_destroy
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 7.0, take #2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  6 Mar 2026 11:22:31 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 Linux 7.0 版本中的修复补丁（patch）。本周的邮件由 Marc Zyngier 提出，主要内容是提交第二批修复补丁，特别关注 pKVM 的一个重要修复，该修复解决了当内存块未按页对齐时，主机无法继续前进的问题。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测，KVM/arm64 的修复工作一直在进行，涉及到一些低严重性的问题，尤其是在页面表代码和 S2 故障处理路径中的修复。这些问题的修复旨在提升系统的稳定性和性能。

本周的新进展包括一系列低严重性错误的修复，具体包括：
1. 修复 S2 故障处理中的几个小错误。
2. 解决在 vgic 初始化过程中可能导致未初始化 vgic 被破坏的问题。
3. 处理 pKVM 启动失败的情况。
4. 增强 NV 阶段 2 的检查，以确保其符合广告的物理地址大小。
5. 移除在模拟 EL2 S1 地址转换时不必要的 ISB 指令。

这些修复将被合并到 KVM/arm64 的 Git 仓库中，以便进一步测试和应用。

#### 📝 邮件列表

1. **[03-06 11:22]** [GIT PULL] KVM/arm64 fixes for 7.0, take #2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/5] basic EL1/EL0 guest support

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  6 Mar 2026 14:26:51 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 KVM 单元测试添加基本的 EL1/EL0 客户支持，包含五个补丁。

1. **原始补丁内容**：该补丁集的目的是为在 EL1 和 EL0 级别运行代码提供基础设施，主要用于编写不需要单独地址空间和多个上下文的简单测试。补丁包括线程信息助手、堆栈操作宏、上下文切换功能、EL0/EL1 客户功能以及超管陷阱测试。

2. **之前讨论要点**：虽然邮件中没有详细的历史讨论，但补丁的设计目标是简化在不同异常级别（EL1 和 EL0）下的测试执行，确保能够在不复杂化上下文管理的情况下进行基本的功能测试。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括：
   - 增加线程信息助手和堆栈操作宏，以便更好地管理线程和堆栈。
   - 实现了根据上下文切换 SP_EL0 和 SP_EL1 的功能。
   - 添加了运行在 EL1 和 EL0 的功能函数，并确保它们共享相同的地址空间。
   - 最后，增加了一个超管陷阱测试，验证在不同异常级别下的行为。

整体来看，本周的讨论和补丁提交为 KVM 的 EL1/EL0 支持奠定了基础，推动了相关测试的开发。

#### 📝 邮件列表

1. **[03-06 14:26]** [kvm-unit-tests PATCH v1 0/5] basic EL1/EL0 guest support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[03-06 14:26]** [kvm-unit-tests PATCH v1 1/5] arm64: add thread_info helpers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[03-06 14:26]** [kvm-unit-tests PATCH v1 2/5] arm64: add macros for manipulating SP
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[03-06 14:26]** [kvm-unit-tests PATCH v1 3/5] arm64: context switch SP_EL0/SP_EL1 depending on context
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[03-06 14:26]** [kvm-unit-tests PATCH v1 4/5] arm64: add EL0/EL1 guest functionality
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[03-06 14:26]** [kvm-unit-tests PATCH v1 5/5] arm64: add hypervisor trapping test
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

