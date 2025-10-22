# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:46:55

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 301
- **总 Thread 数**: 26
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 22 threads (294 邮件)
- **RFC**: 2 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 1 threads (2 邮件)

---

## 📌 PATCH

共 22 个 thread

---

### Thread 1: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 36 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 16:02:41 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上实现 SCTLR2、DoubleFault2 和 NV 外部中止的修复补丁系列（PATCH v2 00/27）。该系列补丁旨在增强 KVM 对新特性的支持，特别是与异常处理和错误注入相关的功能。

**原始补丁/问题内容**：
补丁系列主要包括对 SCTLR2、DoubleFault2 和 NV 外部中止的支持，解决了在 KVM 中处理这些特性时的多个问题。补丁的关键在于实现了 FEAT_RAS（错误处理特性）、FEAT_SCTLR2 和 FEAT_DoubleFault2。

**之前讨论要点**：
在历史讨论中，开发者们对补丁的初步版本进行了反馈，提出了对异常处理和错误注入的改进建议，包括如何处理嵌套上下文中的错误状态和异常路由。

**本周新讨论、新进展或结论**：
本周的讨论集中在补丁的具体实现和测试上，Oliver Upton 提出了多个补丁，涵盖了对异常路由、错误注入和状态管理的改进。Marc Zyngier 对部分补丁进行了审查，提出了一些建议和问题，特别是关于如何处理嵌套虚拟机中的异常和错误状态的传递。最终，Marc 对补丁系列表示认可，并给予了“Reviewed-by”的标记，表明他认为这些补丁在解决问题上是有效的。

整体来看，本周的讨论推动了对 KVM 在 ARM64 上新特性支持的进一步完善，并为后续的开发和测试奠定了基础。

#### 📝 邮件列表

1. **[06-16 16:02]** [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-16 16:02]** [PATCH v2 01/27] arm64: Detect FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 16:02]** [PATCH v2 02/27] arm64: Detect FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[06-16 16:02]** [PATCH v2 03/27] KVM: arm64: Add helper to identify a nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[06-16 16:02]** [PATCH v2 04/27] KVM: arm64: Treat vCPU with pending SError as runnable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[06-16 16:02]** [PATCH v2 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-16 16:02]** [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-16 16:02]** [PATCH v2 07/27] KVM: arm64: nv: Add FEAT_RAS vSError sys regs to table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-16 16:02]** [PATCH v2 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-16 16:02]** [PATCH v2 09/27] KVM: arm64: nv: Advertise support for FEAT_RAS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[06-16 16:02]** [PATCH v2 10/27] KVM: arm64: nv: Describe trap behavior of SCTLR2_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[06-16 16:02]** [PATCH v2 11/27] KVM: arm64: Wire up SCTLR2_ELx sysreg descriptors
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[06-16 16:02]** [PATCH v2 12/27] KVM: arm64: Context switch SCTLR2_ELx when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[06-16 16:02]** [PATCH v2 13/27] KVM: arm64: Enable SCTLR2 when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[06-16 16:02]** [PATCH v2 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[06-16 16:02]** [PATCH v2 15/27] KVM: arm64: Factor out helper for selecting exception target EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[06-16 16:02]** [PATCH v2 16/27] KVM: arm64: nv: Ensure Address size faults affect correct ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[06-16 16:02]** [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[06-16 16:02]** [PATCH v2 18/27] KVM: arm64: nv: Handle effects of HCRX_EL2.TMEA on SError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[06-16 16:03]** [PATCH v2 19/27] KVM: arm64: Take "masked" SEAs to EL2 when TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[06-16 16:03]** [PATCH v2 20/27] KVM: arm64: nv: Enable vSErrors when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[06-16 16:03]** [PATCH v2 21/27] KVM: arm64: Advertise support for FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[06-16 16:03]** [PATCH v2 22/27] KVM: arm64: Advertise support for FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[06-16 16:03]** [PATCH v2 23/27] KVM: arm64: Don't retire MMIO instruction w/ pending (emulated) SError
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
25. **[06-16 16:03]** [PATCH v2 24/27] KVM: arm64: selftests: Add basic SError injection test
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[06-16 16:03]** [PATCH v2 25/27] KVM: arm64: selftests: Test SEAs are taken to SError vector when EASE=1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[06-16 16:03]** [PATCH v2 26/27] KVM: arm64: selftests: Add SCTLR2_EL1 to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-16 16:03]** [PATCH v2 27/27] KVM: arm64: selftests: Catch up set_id_regs with the kernel
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[06-21 10:51]** Re: [PATCH v2 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[06-21 11:47]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[06-21 12:09]** Re: [PATCH v2 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[06-21 12:34]** Re: [PATCH v2 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[06-21 12:54]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[06-21 14:03]** Re: [PATCH v2 18/27] KVM: arm64: nv: Handle effects of HCRX_EL2.TMEA on SError injection
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[06-22 09:39]** Re: [PATCH v2 19/27] KVM: arm64: Take "masked" SEAs to EL2 when TMEA is set
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[06-22 10:25]** Re: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 33 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM 的 IOMMU 设备中断支持的重大改进，具体是针对设备发布中断（posted IRQs）的支持进行全面重构。该讨论包含了 62 个补丁，其中第一个补丁是针对 arm64 的修复，建议在 6.16 版本中合并。

在历史讨论中，主要集中在多个补丁的细节上，包括如何处理 IRQ 路由条目的类型变化、在解映射虚拟本地外部中断（vLPI）失败时发出警告等。参与者们对补丁的有效性和潜在影响进行了深入探讨，尤其是对 ARM 和 x86 体系结构的不同处理方式进行了比较。

在本周的新讨论中，参与者 Naveen N Rao 对多个补丁提出了具体的改进建议，并对补丁的可读性和逻辑进行了审查。特别是关于如何处理 APICv 的启用和禁用问题，Naveen 提出了更清晰的实现方案。此外，Sean Christopherson 也对补丁的依赖关系和潜在的内存管理问题进行了讨论，强调了在 vCPU 创建过程中需要谨慎处理的细节。

总体来看，本周的讨论推动了补丁的进一步完善，确保了 KVM 在处理设备中断时的稳定性和性能。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead of
 rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-11 15:45]** [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on ID
 during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-11 15:45]** [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-11 15:45]** [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC Physical
 ID entry pointer
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-11 15:45]** [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE
 updates in IOMMU
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-12 12:59]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-12 07:34]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-13 13:47]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[06-17 19:55]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Naveen N Rao <naveen@kernel.org>
14. **[06-17 20:19]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Naveen N Rao <naveen@kernel.org>
15. **[06-17 20:31]** Re: [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Naveen N Rao <naveen@kernel.org>
16. **[06-17 21:12]** Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across
 IRTE updates in IOMMU
   - 发件人: Naveen N Rao <naveen@kernel.org>
17. **[06-17 09:10]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[06-17 09:33]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-18 20:03]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Naveen N Rao <naveen.rao@amd.com>
20. **[06-18 20:09]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Naveen N Rao <naveen.rao@amd.com>
21. **[06-18 13:59]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[06-19 16:39]** Re: [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC
 Physical ID entry pointer
   - 发件人: Naveen N Rao <naveen@kernel.org>
23. **[06-19 17:01]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
24. **[06-19 17:31]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
25. **[06-19 13:36]** Re: (subset) [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type changes as changes
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[06-20 07:39]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-20 10:22]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-20 19:00]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: David Woodhouse <dwmw2@infradead.org>
29. **[06-20 11:48]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[06-20 12:04]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[06-20 12:27]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
32. **[06-20 13:31]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[06-20 13:45]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 3: [PATCH v2 00/23] ARM64 PMU Partitioning

**📧 邮件数**: 31 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 22:13:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区的补丁系列，主要由 Colton Lewis 提出。以下是讨论的主要内容：

1. **原始补丁内容**：该补丁系列旨在实现 ARM 架构的分区 PMU 方案，允许为虚拟机（VM）保留一部分计数器，以减少开销并提高性能。补丁包括对命令行参数和 ioctl 的语义更改，以支持在运行时对 PMU 进行分区。

2. **历史讨论要点**：之前的讨论集中在如何有效地管理 PMU 的分区，确保在不同 CPU 上的异构硬件中正确处理计数器的分配。参与者还讨论了如何在不影响性能的情况下实现 PMU 的分区，并确保虚拟机能够直接访问所需的硬件计数器。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现和细节上，包括：
   - 引入了新的模块参数以配置 PMU 分区。
   - 讨论了如何在没有 FGT（细粒度陷阱）支持的情况下处理 PMU 访问。
   - 进行了多次代码审查，确保补丁符合内核的整体设计原则。
   - 参与者提出了对补丁的反馈，建议使用更简洁的参数来描述主机使用的计数器数量，并确保 KVM 能够发现剩余的计数器。

总结来说，本周的讨论推动了 ARM64 PMU 分区补丁的完善，确保其在 KVM 中的有效性和性能优化。

#### 📝 邮件列表

1. **[06-20 22:13]** [PATCH v2 00/23] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-20 22:13]** [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-20 22:13]** [PATCH v2 02/23] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-20 22:13]** [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-20 22:13]** [PATCH v2 04/23] arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-20 22:13]** [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-20 22:13]** [PATCH v2 06/23] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-20 22:13]** [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[06-20 22:13]** [PATCH v2 07/23] perf: pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[06-20 22:13]** [PATCH v2 08/23] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-20 22:13]** [PATCH v2 09/23] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[06-20 22:13]** [PATCH v2 10/23] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[06-20 22:13]** [PATCH v2 11/23] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[06-20 22:13]** [PATCH v2 12/23] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[06-20 22:13]** [PATCH v2 13/23] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[06-20 22:13]** [PATCH v2 14/23] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[06-20 22:13]** [PATCH v2 15/23] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[06-20 22:13]** [PATCH v2 16/23] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[06-20 22:13]** [PATCH v2 17/23] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[06-20 22:13]** [PATCH v2 18/23] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[06-20 22:13]** [PATCH v2 19/23] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[06-20 22:13]** [PATCH v2 20/23] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[06-20 22:13]** [PATCH v2 20/23] perf: pmuv3: Handle IRQs for Partitioned PMU guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[06-20 22:13]** [PATCH v2 21/23] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
25. **[06-20 22:13]** [PATCH v2 22/23] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
26. **[06-20 22:13]** [PATCH v2 23/23] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
27. **[06-20 17:44]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-20 17:45]** Re: [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[06-20 18:06]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[06-21 22:56]** Re: [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: kernel test robot <lkp@intel.com>
31. **[06-22 17:32]** Re: [PATCH v2 17/23] KVM: arm64: Account for partitioning in
 PMCR_EL0 access
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 4: [PATCH v3 00/15] KVM: Introduce KVM Userfault

**📧 邮件数**: 29 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 18 Jun 2025 04:24:09 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM Userfault 的引入，主要由 James Houghton 提出了一系列补丁（PATCH v3 00/15）。该补丁旨在解决现有 KVM 中缺乏用户故障处理机制的问题，特别是在进行后拷贝实时迁移时。

**原始补丁内容**：
KVM Userfault 提供了一种机制，使得在启用 KVM_MEM_USERFAULT 的内存槽中，用户可以通过 bitmap 指定哪些页面的访问会导致 KVM 退出到用户空间。这种机制旨在提高用户故障处理的效率，特别是在大规模虚拟 CPU 的场景下。

**之前讨论要点**：
在之前的讨论中，补丁的设计和实现细节得到了反馈，特别是如何处理不同架构（如 x86 和 arm64）中的用户故障。参与者们讨论了如何在结构体中整合故障信息，以及如何优化 KVM 的内存管理。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括对结构体 `kvm_page_fault` 的定义、用户故障的处理逻辑，以及如何在 x86 和 arm64 架构中实现用户故障退出。参与者们提出了对返回值类型的建议，讨论了如何更好地处理故障标志，以及在文档中增加 KVM_CAP_USERFAULT 和 KVM_MEM_USERFAULT 的细节。此外，针对自测代码的改进也得到了关注，确保新功能的正确性和稳定性。

总结来说，本周的讨论推动了 KVM Userfault 的实现进展，参与者们积极反馈并提出改进建议，为最终合并补丁奠定了基础。

#### 📝 邮件列表

1. **[06-18 04:24]** [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: James Houghton <jthoughton@google.com>
2. **[06-18 04:24]** [PATCH v3 01/15] KVM: x86/mmu: Move "struct kvm_page_fault"
 definition to asm/kvm_host.h
   - 发件人: James Houghton <jthoughton@google.com>
3. **[06-18 04:24]** [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to gather
 common fault variables
   - 发件人: James Houghton <jthoughton@google.com>
4. **[06-18 04:24]** [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault" for
 memory fault exits
   - 发件人: James Houghton <jthoughton@google.com>
5. **[06-18 04:24]** [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
6. **[06-18 04:24]** [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
7. **[06-18 04:24]** [PATCH v3 06/15] KVM: arm64: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
8. **[06-18 04:24]** [PATCH v3 07/15] KVM: Enable and advertise support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
9. **[06-18 04:24]** [PATCH v3 08/15] KVM: selftests: Fix vm_mem_region_set_flags docstring
   - 发件人: James Houghton <jthoughton@google.com>
10. **[06-18 04:24]** [PATCH v3 09/15] KVM: selftests: Fix prefault_mem logic
   - 发件人: James Houghton <jthoughton@google.com>
11. **[06-18 04:24]** [PATCH v3 10/15] KVM: selftests: Add va_start/end into uffd_desc
   - 发件人: James Houghton <jthoughton@google.com>
12. **[06-18 04:24]** [PATCH v3 11/15] KVM: selftests: Add KVM Userfault mode to demand_paging_test
   - 发件人: James Houghton <jthoughton@google.com>
13. **[06-18 04:24]** [PATCH v3 12/15] KVM: selftests: Inform set_memory_region_test of KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>
14. **[06-18 04:24]** [PATCH v3 13/15] KVM: selftests: Add KVM_MEM_USERFAULT + guest_memfd
 toggle tests
   - 发件人: James Houghton <jthoughton@google.com>
15. **[06-18 04:24]** [PATCH v3 14/15] KVM: Documentation: Fix section number for KVM_CAP_ARM_WRITABLE_IMP_ID_REGS
   - 发件人: James Houghton <jthoughton@google.com>
16. **[06-18 04:24]** [PATCH v3 15/15] KVM: Documentation: Add KVM_CAP_USERFAULT and
 KVM_MEM_USERFAULT details
   - 发件人: James Houghton <jthoughton@google.com>
17. **[06-18 12:26]** Re: [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to
 gather common fault variables
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[06-18 12:40]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM
 Userfaults
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[06-18 13:00]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct
 kvm_page_fault" for memory fault exits
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[06-18 13:33]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[06-18 13:38]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
22. **[06-18 13:41]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
23. **[06-18 13:47]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault"
 for memory fault exits
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[06-18 14:17]** Re: [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to
 gather common fault variables
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[06-18 15:43]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM
 Userfaults
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[06-18 16:14]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct
 kvm_page_fault" for memory fault exits
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[06-18 16:24]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-18 18:22]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault"
 for memory fault exits
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[06-18 18:27]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 5: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 28 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中支持映射基于 guest_memfd 的内存，以增强软件保护虚拟机的功能。原始的 patch 系列（[PATCH v12 00/18]）旨在允许主机映射 guest_memfd 支持的内存，这对于像 Firecracker 这样的虚拟机管理程序非常重要，能够增强对 Spectre 类攻击的防护。

在历史讨论中，参与者们关注了 patch 的命名和功能描述，特别是对 `kvm->arch.has_private_mem` 的重命名为 `kvm->arch.supports_gmem` 的合理性，以及如何清晰地表达内存的共享和私有特性。讨论中提到，现有的命名可能会导致混淆，特别是在共享和私有内存的定义上。

在本周的新讨论中，参与者们继续探讨了命名的准确性和清晰性，特别是关于 `GUEST_MEMFD_FLAG_SUPPORT_SHARED` 和 `GUEST_MEMFD_FLAG_MMAP` 的使用。讨论中提到，虽然“共享”一词在某些上下文中是直观的，但在非 CoCo 虚拟机中可能会引起误解。参与者们一致认为需要在命名上达成共识，以便在后续的 patch 中进行修改。

总的来说，本周的讨论集中在 patch 的命名、功能描述的清晰性以及如何更好地表达内存的共享和私有特性上，以确保后续开发的顺利进行。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-13 14:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-16 07:52]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-16 08:13]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[06-16 08:44]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map
 guest_memfd pages
   - 发件人: Ira Weiny <ira.weiny@intel.com>
9. **[06-16 16:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[06-16 15:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-16 16:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
12. **[06-16 16:20]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to
 kvm->arch.supports_gmem
   - 发件人: David Hildenbrand <david@redhat.com>
13. **[06-16 16:25]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
14. **[06-17 16:04]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[06-17 17:40]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[06-18 10:15]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
17. **[06-18 17:20]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
18. **[06-18 11:25]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
19. **[06-18 11:27]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
20. **[06-18 17:44]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
21. **[06-18 11:59]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
22. **[06-18 18:42]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
23. **[06-18 13:14]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
24. **[06-18 12:18]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
25. **[06-18 20:17]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
26. **[06-18 15:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
27. **[06-18 18:48]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-18 18:50]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 6: [PATCH v7 0/5] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 18 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 18 Jun 2025 06:55:36 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM (Kernel-based Virtual Machine) 在 arm64 架构下映射 GPU 设备内存为可缓存的补丁（PATCH v7 0/5）。该补丁旨在解决当前 KVM 对设备内存的映射限制，允许将 GPU 设备内存标记为可缓存，以提高性能。

**历史讨论要点**：
补丁的背景是，现有的 KVM 代码限制了设备内存的映射方式，导致未添加到内核的设备内存无法被标记为可缓存。补丁通过检查 VMA（虚拟内存区域）的 pgprot 值来判断可缓存性，从而允许安全地将 PFNMAP（页面框架号映射）标记为可缓存。

**本周新讨论进展**：
1. **补丁细节**：补丁分为五个部分，涵盖了重命名符号、阻止不匹配的缓存属性、添加硬件缓存管理支持的函数、允许基于 VMA 标志的可缓存映射，以及暴露新的 KVM 能力以供用户空间查询。
2. **反馈与修改**：参与者对补丁提出了多项建议，包括变量命名的清晰性、是否需要初始化某些变量等。Ankit Agrawal（补丁作者）表示将根据反馈进行相应修改。
3. **安全性考虑**：讨论中强调了防止缓存不一致性和安全风险的重要性，尤其是在不同虚拟机之间共享内存时。

总体而言，本周的讨论集中在补丁的具体实现和潜在的安全性问题上，参与者积极提供反馈以改进补丁的质量和功能。

#### 📝 邮件列表

1. **[06-18 06:55]** [PATCH v7 0/5] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-18 06:55]** [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO may be used
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-18 06:55]** [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-18 06:55]** [PATCH v7 3/5] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-18 06:55]** [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-18 06:55]** [PATCH v7 5/5] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-18 15:28]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
8. **[06-18 15:35]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[06-18 16:46]** Re: [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[06-18 17:12]** Re: [PATCH v7 3/5] KVM: arm64: New function to determine hardware
 cache management support
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[06-18 17:34]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[06-18 13:38]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
13. **[06-19 02:21]** Re: [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
14. **[06-19 02:22]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
15. **[06-19 12:14]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
16. **[06-19 11:16]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
17. **[06-19 12:03]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Donald Dutile <ddutile@redhat.com>
18. **[06-19 16:46]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 7: [PATCH v8 00/14] arm: rework id register storage

**📧 邮件数**: 16 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 17 Jun 2025 17:39:17 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 ID 寄存器存储的重构工作，主要涉及一系列补丁（PATCH v8 00/14 至 14/14），由 Eric Auger 提出，Cornelia Huck 进行维护。

1. **原始补丁内容**：补丁旨在重构 ARM 架构的 ID 寄存器存储方式，主要通过将寄存器定义从结构体转移到数组中，以便更好地支持 KVM 和 CPU 模型的扩展。

2. **历史讨论要点**：之前的讨论集中在如何改进寄存器定义的生成和管理。补丁系列经过多次迭代，逐步解决了反馈问题，增强了脚本的健壮性，并确保生成的文件符合最新的 Linux sysregs 结构。

3. **本周的新讨论与进展**：
   - 本周的邮件中，Eric Auger 提出了新的补丁，增加了系统寄存器生成脚本，简化了寄存器定义的生成过程，确保其与 Linux 源树的兼容性。
   - 讨论中提到，生成的寄存器定义文件将被用于替代手动维护的寄存器定义，从而提高代码的可维护性和一致性。
   - 最后，Cornelia Huck 提到在使用 checkpatch.pl 工具时遇到的许可证问题，强调了代码提交时需要遵循的许可证要求。

整体来看，本次讨论的核心是通过自动化脚本来优化 ARM ID 寄存器的管理和定义，提高代码质量和维护效率。

#### 📝 邮件列表

1. **[06-17 17:39]** [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-17 17:39]** [PATCH v8 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[06-17 17:39]** [PATCH v8 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[06-17 17:39]** [PATCH v8 03/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[06-17 17:39]** [PATCH v8 04/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[06-17 17:39]** [PATCH v8 05/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[06-17 17:39]** [PATCH v8 06/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-17 17:39]** [PATCH v8 07/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[06-17 17:39]** [PATCH v8 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[06-17 17:39]** [PATCH v8 09/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[06-17 17:39]** [PATCH v8 10/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[06-17 17:39]** [PATCH v8 11/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[06-17 17:39]** [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[06-17 17:39]** [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[06-17 17:39]** [PATCH v8 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Cornelia Huck <cohuck@redhat.com>
16. **[06-17 17:45]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 8: [PATCH v4 0/5] Add FIELD_MODIFY() helper

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 12 Jun 2025 21:46:07 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是新增的 `FIELD_MODIFY()` 辅助宏，旨在增强位域操作的类型检查。历史讨论中，Luo Jie 提出了一个包含五个补丁的系列，主要目的是将 `FIELD_MODIFY()` 作为现有位域宏的补充，提供编译时参数类型检查，并对内核中的四个实例进行了转换。Marc Zyngier 对此表示反对，认为现有的辅助函数已经足够，不需要增加重复的功能。

在本周的新讨论中，Luo Jie 决定在下一个版本中删除 ARM64 的补丁，仅保留 Coccinelle 脚本补丁。Markus Elfring 提出了一些关于补丁描述和格式化的建议，Luo Jie 表示会在下次修订中采纳这些建议。Will Deacon 则质疑 `FIELD_MODIFY()` 的必要性，要求更详细地解释其相较于现有功能的优势。Luo Jie 进一步澄清，尽管 `FIELD_MODIFY()` 提供了严格的参数类型检查，但在 ARM64 的特定情况下，现有的 `FIELD_PREP()` 已经能够满足这一需求，因此可能没有额外的好处。

总体来看，本周的讨论集中在补丁的必要性和格式改进上，尚未达成明确的结论。

#### 📝 邮件列表

1. **[06-12 21:46]** [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-12 21:46]** [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[06-12 21:46]** [PATCH v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[06-12 15:11]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-12 18:48]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
6. **[06-12 22:15]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
7. **[06-16 18:06]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
8. **[06-16 18:28]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
9. **[06-16 18:37]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
10. **[06-16 11:41]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Will Deacon <will@kernel.org>
11. **[06-16 15:52]** Re: [cocci] [v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
12. **[06-17 00:19]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
13. **[06-17 00:19]** Re: [cocci] [v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 9: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 16:07:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 GICv5 主机支持 GICv3 客户机的补丁系列，主要集中在如何处理转发的 PPI 中断和兼容性问题。

1. **原始补丁内容**：
   - 第一个补丁（[PATCH 1/5]）提出在转发给客户机的 PPI 中断中跳过停用操作，仅执行结束中断（EOI）。这依赖于客户机稍后处理注入中断时自行停用虚拟和物理中断，模仿 GICv3 的原生行为。

2. **之前讨论要点**：
   - 该补丁是为在 GICv5 主机上添加 GICv3 兼容模式的支持而设计，确保转发的 PPI 行为与 GICv3 的期望一致，且无需对现有的 GICv3 虚拟机或虚拟机监控程序进行修改。

3. **本周的新讨论与进展**：
   - 本周的讨论中，Sascha Bischoff 提出了多个补丁，涵盖了 GICv5 的初始化、系统寄存器的添加以及 KVM 对 GICv5 的探测支持。Oliver Upton 提出了一些改进建议，包括简化代码和确保与用户API的兼容性。讨论中还提到了一些实现细节和未来的架构修订，强调了对 GICv5 的支持将如何影响虚拟机的迁移和上下文同步。

总之，本周的讨论推动了 GICv5 对 GICv3 客户机支持的实现，确保了兼容性和功能的完整性。

#### 📝 邮件列表

1. **[06-20 16:07]** [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-20 16:07]** [PATCH 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-20 16:07]** [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-20 16:07]** [PATCH 3/5] arm64/sysreg: Add ICH_VCTLR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-20 16:07]** [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-20 16:07]** [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[06-20 13:20]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-20 13:25]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-20 16:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-22 13:19]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-22 05:37]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 10 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm64 架构在 KVM 中支持 Arm CCA 的补丁（PATCH v9 00/43）。该补丁系列旨在实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 版本中合并，补丁中提到的 NV 支持也已上游。

在历史讨论中，Steven Price 提出了多个补丁，涉及创建和配置领域（realm）、RTT 的销毁、VMM 设置 RIPAS 以及运行时内存故障处理等功能。这些补丁的目标是增强 KVM 对 Arm CCA 的支持，确保虚拟机在受保护环境中的安全性和性能。

本周的新讨论主要集中在补丁的细节修正和潜在问题上。Suzuki K Poulose 提出了对 RTT 销毁过程中的代码注释和逻辑的改进建议。Gavin Shan 指出在内存映射过程中可能导致 RCU 停滞的问题，并建议将 `@may_block` 设置为 true。Yiwei Zhuang 询问在某个分支中是否应释放和撤销 RTT，而 Andre Przywara 则报告了在 GCC 10 下的构建错误，并提供了修复建议。

总体来看，本周的讨论主要围绕补丁的细节优化和潜在的构建问题，参与者们积极提供反馈，以确保补丁的质量和稳定性。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-16 11:41]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[06-16 11:47]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[06-16 21:55]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[06-17 20:56]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
10. **[06-18 13:33]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 11: [PATCH v8 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 12:09:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下如何将 GPU 设备内存映射为可缓存的内存。Ankit Agrawal 提出了一个补丁系列（PATCH v8 0/6），旨在解决当前 KVM 对设备内存的映射限制，特别是在 Grace Hopper 和 Blackwell 超级芯片平台上。

**原始补丁内容**：补丁的核心是允许 GPU 设备内存被标记为可缓存，这样可以提高性能。当前 KVM 强制将内存区域映射为 NORMAL 或 DEVICE_nGnRE，限制了未添加到内核的设备内存的缓存能力。

**之前讨论要点**：在历史讨论中，维护者们提出了多项建议，帮助优化补丁的实现，包括变量重命名、代码结构调整以及安全性检查等。补丁经过多次迭代，逐步完善。

**本周新讨论及进展**：本周的讨论集中在补丁的具体实现上，包括对设备内存检测的更新、阻止缓存 PFNMAP 映射的安全性修复、以及引入新函数以确认硬件缓存管理支持等。Ankit 还引入了一个新的 KVM 能力标志，允许用户空间查询是否支持缓存 PFNMAP 映射。Jason Gunthorpe 提出了对补丁逻辑的进一步优化建议，Ankit 表示将根据反馈进行调整。

整体来看，本周的讨论推动了补丁的进一步完善，确保了 KVM 在处理 GPU 设备内存时的安全性和性能。

#### 📝 邮件列表

1. **[06-20 12:09]** [PATCH v8 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-20 12:09]** [PATCH v8 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-20 12:09]** [PATCH v8 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-20 12:09]** [PATCH v8 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-20 12:09]** [PATCH v8 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-20 12:09]** [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-20 12:09]** [PATCH v8 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
8. **[06-20 09:20]** Re: [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
9. **[06-20 13:07]** Re: [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 12: [PATCH 0/7] KVM: arm64: trap fixes and cleanup

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 17 Jun 2025 14:37:11 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 在 arm64 架构下的 trap 修复和清理工作，包含七个补丁（patch）。这些补丁主要解决了 VHE 模式下 KVM 管理 traps 的一些问题，并进行了相应的代码清理。

**原始补丁内容**：
补丁系列的核心内容包括：
1. 修复调试寄存器操作中的理论问题。
2. 解决由于来宾 hypervisor 配置 CPTR_EL2 导致主机意外捕获 traps 的问题。
3. 修正来宾 hypervisor 配置 CPTR_EL2 时未能正确处理 SVE 使用的问题。

**之前讨论要点**：
在之前的讨论中，Mark Rutland 提到他在实现代码清理时发现了 CPTR trap 管理存在的问题，并指出调试寄存器配置的潜在风险。补丁的设计基于对现有代码的检查和测试。

**本周的新讨论与进展**：
本周的讨论中，Mark Rutland 提交了七个补丁的具体实现，并进行了初步测试。他请求社区的进一步测试和审查。最终，Marc Zyngier 确认了这些补丁并将其应用于修复集。这些补丁的应用将有助于提高 KVM 在 arm64 架构下的稳定性和性能。

#### 📝 邮件列表

1. **[06-17 14:37]** [PATCH 0/7] KVM: arm64: trap fixes and cleanup
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[06-17 14:37]** [PATCH 1/7] KVM: arm64: VHE: Synchronize restore of host debug registers
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[06-17 14:37]** [PATCH 2/7] KVM: arm64: VHE: Synchronize CPTR trap deactivation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
4. **[06-17 14:37]** [PATCH 3/7] KVM: arm64: Reorganise CPTR trap manipulation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[06-17 14:37]** [PATCH 4/7] KVM: arm64: Remove ad-hoc CPTR manipulation from fpsimd_sve_sync()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
6. **[06-17 14:37]** [PATCH 5/7] KVM: arm64: Remove ad-hoc CPTR manipulation from kvm_hyp_handle_fpsimd()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[06-17 14:37]** [PATCH 6/7] KVM: arm64: Remove cpacr_clear_set()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
8. **[06-17 14:37]** [PATCH 7/7] KVM: arm64: VHE: Centralize ISBs when returning to host
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[06-19 13:36]** Re: [PATCH 0/7] KVM: arm64: trap fixes and cleanup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v5 0/6] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 09:02:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FF-A 1.2 及 SEND_DIRECT2 ABI 的支持，主要由 Per Larsen 提出了一系列补丁（patch）。

1. **原始补丁内容**：补丁集的目标是实现 FF-A 1.2 规范中的新 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载，并确保主机不会使用低于已经与虚拟机监控器协商的 FF-A 版本。补丁还包括对 SMCCC 1.2 的支持，这是 FF-A 1.2 所必需的。

2. **之前讨论要点**：在之前的讨论中，补丁集经过多次修改，主要集中在如何安全地处理不同版本的 FF-A 和 SMCCC 之间的兼容性，以及如何实现新接口的功能。参与者对补丁的设计和实现细节进行了反复讨论，确保新功能的稳定性和向后兼容性。

3. **本周的新讨论与进展**：本周的讨论主要集中在 Per Larsen 提出的六个补丁上，包括修复主机版本降级的返回值、在初始化中使用 SMCCC 1.2、标记不支持的 FFA_NOTIFICATION_* 调用，以及实现 FFA_MSG_SEND_DIRECT_REQ2 接口。Marc Zyngier 对某些补丁的命名和实现方式提出了批评，认为不必要的变量重命名增加了代码的复杂性，建议保持一致性以提高可读性。

总体而言，本周的讨论推动了对 FF-A 1.2 的支持进展，同时也引发了对代码可读性的关注。

#### 📝 邮件列表

1. **[06-19 09:02]** [PATCH v5 0/6] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[06-19 09:02]** [PATCH v5 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[06-19 09:02]** [PATCH v5 2/6] KVM: arm64: Use SMCCC 1.2 in
 hyp_ffa_{init,post_init}
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[06-19 09:02]** [PATCH v5 3/6] KVM: arm64: Use SMCCC 1.2 in host FF-A handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[06-19 09:02]** [PATCH v5 4/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[06-19 09:02]** [PATCH v5 5/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[06-19 09:02]** [PATCH v5 6/6] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
8. **[06-22 14:01]** Re: [PATCH v5 3/6] KVM: arm64: Use SMCCC 1.2 in host FF-A handler
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH kvmtool 0/3] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 11:44:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁（PATCH kvmtool 0/3）。该补丁包含三个部分：第一部分更新内核头文件以支持新的 EL2 能力和 VGIC 设备控制；第二部分引入了新的命令行选项“--nested”，允许 VCPU 在 EL2 中启动；第三部分则通过设置维护 IRQ 来支持 VGIC。

在历史讨论中，参与者们确认了 ARMv8.3 架构的更新已将嵌套虚拟化支持合并到主线内核中，kvmtool 也应相应更新以支持这一功能。讨论中提到，补丁的实现经过了多次测试，包括在 FVP 和一些商业硬件上。

本周的新讨论中，Andre Przywara 提出了补丁的具体实现细节，并询问是否需要其他补丁。Alexandru Elisei 建议将命令行选项“--nested”改为“--el2”，以更好地与 KVM 的命名一致，但 Marc Zyngier 认为“nested”更能准确描述该功能的效果。最终，参与者们对补丁的必要性和实现细节达成了一致，补丁的推进得到了积极的反馈。

#### 📝 邮件列表

1. **[06-20 11:44]** [PATCH kvmtool 0/3] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[06-20 11:44]** [PATCH kvmtool 1/3] Sync kernel UAPI headers with v6.16-rc1
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[06-20 11:44]** [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[06-20 11:44]** [PATCH kvmtool 3/3] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[06-20 12:09]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[06-20 12:13]** Re: [PATCH kvmtool 0/3] arm64: Nested virtualization support
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[06-20 12:52]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[06-20 14:43]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 15: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 14 Jun 2025 22:57:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是修复 KVM 中 arm64 架构的 vgic_v3_put_nested() 函数中 s_cpu_if->vgic_lr[] 的索引问题。历史讨论中，Wei-Lin Chang 提出了一个补丁，指出 s_cpu_if->vgic_lr[] 的填充方式与索引方式不一致，建议修正索引逻辑，以确保正确性。

在本周的新讨论中，Oliver Upton 对补丁的变更日志提出了改进建议，认为应更清晰地描述问题背景，并表示补丁本身没有问题，给予了审核通过。Marc Zyngier 也对补丁表示赞赏，并提出应考虑消除双重索引，以降低出错风险。他提出了一个更大的补丁，旨在通过简化索引逻辑来解决问题，并引入了一些辅助函数来简化代码。Wei-Lin Chang 对此表示支持，并建议改进函数命名以提高可读性。

最终，Marc Zyngier 在补丁中进行了小幅修改，使用 hweight16() 代替 hweight64()，以优化性能。整体来看，本周的讨论集中在补丁的改进和代码的优化上，参与者们积极交流，推动了问题的解决。

#### 📝 邮件列表

1. **[06-14 22:57]** [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[06-15 22:55]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 11:54]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-16 22:34]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
5. **[06-16 22:40]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
6. **[06-16 18:00]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[06-16 21:53]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-17 10:26]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 21 Jun 2025 04:21:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下如何将 GPU 设备内存映射为可缓存的内存。Ankit Agrawal 提出了一个补丁（PATCH v9 0/6），旨在解决当前 KVM 对设备内存的映射限制，允许 GPU 设备内存被标记为可缓存。

在历史讨论中，KVM 目前强制将内存映射为 NORMAL 或 DEVICE_nGnRE，这限制了未添加到内核的设备内存无法被标记为可缓存。补丁的主要目标是通过检查 VMA（虚拟内存区域）的 pgprot 值，确保在合适的条件下将设备内存映射为可缓存。

本周的新讨论中，Ankit 提出了多个补丁，主要包括：
1. **重命名变量**：将“device”变量重命名为“s2_force_noncacheable”，以更准确地反映其功能。
2. **更新设备内存检测**：改进了对设备内存的检测逻辑，确保只在适当的情况下调用。
3. **阻止缓存 PFNMAP 映射**：修复了由于 S1 和 S2 映射属性不匹配而导致的安全漏洞。
4. **新函数**：添加了一个函数以确定硬件是否支持缓存管理。
5. **允许 VMA 标志的缓存映射**：允许根据 VMA 的标志进行缓存映射，前提是硬件支持。
6. **暴露新的 KVM 能力**：引入了一个新的 KVM 能力，向用户空间指示是否支持缓存 PFNMAP 的映射。

这些补丁的实施将使得 KVM 在处理 GPU 设备内存时更加灵活和安全，特别是在 Grace Hopper 和 Blackwell 超级芯片等平台上。整体讨论显示出对补丁的积极反馈和对其潜在影响的认可。

#### 📝 邮件列表

1. **[06-21 04:21]** [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-21 04:21]** [PATCH v9 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-21 04:21]** [PATCH v9 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-21 04:21]** [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-21 04:21]** [PATCH v9 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-21 04:21]** [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-21 04:21]** [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>

---

### Thread 17: [PATCH 0/8] KVM: Remove include/kvm, standardize includes

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 17:10:34 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“[PATCH 0/8] KVM: 移除 include/kvm，标准化包含文件”。该补丁旨在通过文件移动和重命名，清理并标准化 KVM 在不同架构下的包含文件。

在历史讨论中，Sean Christopherson 提出了多个补丁，主要包括将 ARM 特定的头文件移动到架构目录、将 iodev.h 移动到标准的 include/linux 目录，以及停止在 PPC 的包含路径中添加 virt/kvm。这些补丁的目标是简化 KVM 的代码结构，并为后续的分区 PMU 工作做好准备。

在本周的新讨论中，Bibo Mao 和 Gautam Menghani 分别对补丁 4 和 6 进行了审核，表示支持。Zenghui Yu 指出，KVM/arm64 MAINTAINERS 中与 ARM 相关的条目可以删除，进一步确认了补丁的有效性和必要性。

总体而言，本周的讨论显示了对补丁的积极反馈，并推动了 KVM 代码的清理和标准化进程。

#### 📝 邮件列表

1. **[06-10 17:10]** [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-10 17:10]** [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm to
 arch directory
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-10 17:10]** [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as kvm_iodev.h
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-10 17:10]** [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-16 09:13]** Re: [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as
 kvm_iodev.h
   - 发件人: Bibo Mao <maobibo@loongson.cn>
6. **[06-16 12:45]** Re: [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include
 path
   - 发件人: Gautam Menghani <gautam@linux.ibm.com>
7. **[06-16 19:10]** Re: [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm
 to arch directory
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 18: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Jun 2025 15:52:34 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在引入一个新的属性以控制 GICD_TYPER2.nASSGIcap。该补丁的主要目的是允许用户在每个虚拟机（VM）基础上控制 GICD_TYPER2.nASSGIcap 的支持，从而解决 GIC 架构中对虚拟处理单元（vPE）数量的限制问题。

在历史讨论中，Raghavendra Rao Ananta 提出了这一补丁，并指出当前 KVM 无条件地在 GICv4.1 系统上广告 GICD_TYPER2.nASSGIcap，建议允许用户在 VGIC 初始化之前更改 VM 是否支持该特性，以便在 vPE ID 受限的环境中进行更灵活的资源分配。

在本周的新讨论中，Marc Zyngier 对补丁提出了建议，要求补充关于默认行为的说明，并质疑在没有 GICv4.1 的情况下是否应该广告 KVM_DEV_ARM_VGIC_FEATURE_nASSGIcap。他认为该 API 应该报告特性是否可配置，以确保与旧版本 KVM 的向后兼容性。

总体来看，本周的讨论集中在补丁的默认行为和向后兼容性问题上，反映出对补丁细节的关注和改进建议。

#### 📝 邮件列表

1. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[06-21 09:50]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 19 Jun 2025 14:48:17 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在移除 `kvm_arch_vcpu_run_map_fp()` 函数。

**原始补丁内容**：补丁的主要目的是删除 `kvm_arch_vcpu_run_map_fp()` 函数。该函数曾用于在运行虚拟 CPU（vCPU）之前，将主机的 FPSIMD 状态映射到 hyp（Hypervisor）Stage-1 映射中。然而，随着两个重要提交的引入（`fbc7e61195e2` 和 `8eca7f6d5100`），主机的 FPSIMD 状态现在在调用 hyp 之前会被主动保存，因此不再需要进行这种映射。

**之前讨论要点**：在历史讨论中，提到过该函数的必要性，但随着内核的演进，相关的映射操作已被简化，导致该函数变得多余。

**本周新讨论及进展**：本周的讨论中，Mark Rutland 提出了补丁，Fuad Tabba 和 Mark Brown 对该补丁进行了测试和审核，均表示支持并确认了补丁的有效性。这表明该补丁得到了积极的反馈，并可能很快被合并到主线代码中。

#### 📝 邮件列表

1. **[06-19 14:48]** [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[06-19 15:35]** Re: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-19 17:28]** Re: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 20: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 6 Jun 2025 10:57:34 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构中引入新的内存槽标志，以指示可缓存映射的补丁（PATCH v6 3/5）。该补丁的初衷是为 KVM 提供一种机制，使得用户空间能够更好地了解内存的缓存属性。

在历史讨论中，参与者 Sean Christopherson 和 Oliver Upton 对该补丁提出了批评。Sean 指出，该补丁在 KVM 的用户 API 中并不合适，并且实现上存在混乱，特别是与 x86 架构的处理不一致。Oliver 也同意这一观点，强调用户空间需要了解其在阶段 1 中的内存状态，以便更好地与 KVM 进行“握手”。

在本周的新讨论中，Ankit Agrawal 感谢了 Sean、Jason 和 Oliver 的反馈，并决定删除该标志，继续在下一个版本中保留 KVM 的能力。这表明他对之前讨论的意见进行了认真考虑，并作出了相应的调整。

#### 📝 邮件列表

1. **[06-06 10:57]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-13 12:38]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 11:37]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable
 mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 21: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 8 Jun 2025 17:54:02 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下自测试的补丁。补丁的主要内容是关闭 GIC（通用中断控制器）文件描述符，以释放其对虚拟机的引用，从而确保能够正确清理虚拟机，并消除在运行 `arch_timer_edge_cases` 测试时出现的 "KVM: debugfs: duplicate directory" 警告。

在历史讨论中，Zenghui Yu 提出了这个补丁，并详细说明了其目的和实现方式，修改了相关的自测试代码文件，以确保在测试完成后能够正确关闭 GIC 文件描述符。

在本周的新讨论中，Marc Zyngier 对该补丁进行了确认，并表示已将其应用到修复列表中。这表明补丁得到了认可并将被纳入后续的代码版本中，显示出讨论的积极进展。

#### 📝 邮件列表

1. **[06-08 17:54]** [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[06-19 13:36]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH v2 09/14] mips: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 19 Jun 2025 16:55:15 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 MIPS 架构中 KCOV 的处理，特别是 __init 和 inline 的不匹配问题。原始的 patch（[PATCH v2 09/14]）旨在解决这一不匹配，以确保在 MIPS 平台上能够正确处理 KCOV 的初始化和内联函数。

在之前的讨论中，Kees Cook 提出了将相关代码标记为 __init，而不是 __always_inline，这一观点得到了支持。Huacai Chen 也表示赞同，认为与 x86 和 arm 的处理方式保持一致是更好的选择。

在本周的新讨论中，Huacai Chen 再次重申了 Kees 的观点，强调应该将相关代码标记为 __init。这表明在 MIPS 架构的 KCOV 处理上，参与者达成了一致意见，倾向于采用 __init 标记，以确保更好的兼容性和性能。整体来看，本周的讨论没有引入新的争议，主要是对之前观点的确认和支持。

#### 📝 邮件列表

1. **[06-19 16:55]** Re: [PATCH v2 09/14] mips: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
2. **[06-19 16:55]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 15:10:15 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests”的补丁，旨在启用 KVM 的嵌套虚拟化自测试。该补丁的核心是实现对嵌套虚拟化环境中多个层级的虚拟机进行自测试，以确保其功能的正确性。

在历史讨论中，参与者们探讨了补丁的设计思路，特别是如何在不同的执行级别（EL）中运行测试代码。Marc Zyngier 提到，默认的测试代码在 EL2 中运行，并且在 VHE（虚拟化扩展）模式下进行。Ganapatrao Kulkarni 也提到，测试的实现需要考虑 L1 和 L0 之间的切换。

在本周的新讨论中，Ganapatrao Kulkarni 对于补丁的实现提出了疑问，特别是关于在运行自测试时是否需要启动完整的客户操作系统。他强调需要的是一种合成测试，能够实现整个虚拟化栈的测试，包括多个层级的客户机和虚拟机监控程序，而不仅仅是在客户机中运行的测试。Marc Zyngier 对此表示了困惑，并重申了 KVM 在嵌套虚拟化中的角色和功能。

总体来看，本周的讨论集中在如何更有效地设计嵌套虚拟化的自测试方案上，参与者们对补丁的具体实现和测试方法进行了深入探讨。

#### 📝 邮件列表

1. **[06-19 15:10]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[06-19 12:45]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in
 EL1

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 19 Jun 2025 16:50:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于通过 KVM 在 EL1 运行 Qualcomm 的 Gunyah Guests 的 RFC PATCH（00/34）。该补丁旨在为 ARM 架构提供一个一致的用户空间 API，以支持不同类型的虚拟化。

在历史讨论中，Marc Zyngier 提出了一个观点，即内核应该为所有硬件提供一致的用户空间 API，包括虚拟化功能。他强调，内核的目标是为用户提供一个统一的接口，而不是在不同平台或硬件上设置限制。他提到，x86 架构已经成功实现了这一点，通过 /dev/kvm 支持 Intel 和 AMD 的不同特性，并且最近还引入了机密计算的支持。

在本周的新讨论中，David Woodhouse 对此进行了回应，重申了内核在提供虚拟化支持方面的重要性。他认为，内核不应当对 ARM 架构的虚拟化功能说“不”，而是应该努力确保其支持所有类型的虚拟化需求。这一讨论强调了在 ARM 平台上实现一致性和全面支持的重要性，反映了对虚拟化技术未来发展的关注。

#### 📝 邮件列表

1. **[06-19 16:50]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in
 EL1
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes, take #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 14:00:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 的第三批修复补丁，主要针对 Linux 6.16 版本。Marc Zyngier 提交的补丁包含了一系列针对浮点（FP）、SIMD 和 SVE 的修复，特别是解决了与 NV 相关的问题，并修补了一些缺失的同步。此外，补丁还涉及中断处理的改进（如路由变更和阴影链接寄存器的错误处理）以及自测修复。

在本周的讨论中，Marc 提到这批补丁的主要内容，包括对 FP/SVE 问题的修复、IRQ 绕过钩子的改进、阴影链接寄存器处理的重构，以及针对 arch_timer_edge_cases 自测的修复。Paolo Bonzini 对补丁表示确认，表示已完成合并。

总体来看，本周的讨论集中在对 KVM/arm64 的重要修复上，解决了多个潜在的错误和同步问题，确保了系统的稳定性和性能。

#### 📝 邮件列表

1. **[06-19 14:00]** [GIT PULL] KVM/arm64 fixes, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[06-20 19:09]** Re: [GIT PULL] KVM/arm64 fixes, take #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 13:34:17 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM 单元测试的补丁，旨在为 arm64 架构支持 EL2（异常级别 2）。本次补丁包含 9 个部分，主要关注如何在 KVM 中正确初始化 EL2。

在历史讨论中，参与者 Joey Gouly 提出了补丁的初步版本，指出当前代码在处理 FEAT_E2H0 特性时存在问题，尤其是在写入 INIT_HCR_EL2_EL1_ONLY 时未能正确检查 KVM 是否支持该特性。

本周的新讨论中，Alexandru Elisei 建议 Joey 考虑直接使用现有的 el2_setup.h 文件中的部分代码，而不是完全自定义初始化代码，以便于后续的更新和修复。Joey 对此表示赞同，并计划基于 Linux 的代码创建一个简化版的 el2_setup.h，以提高代码的可维护性。

总体来看，本周的讨论集中在如何优化 EL2 的初始化过程，并寻求代码复用的可能性，以提升代码质量和维护效率。

#### 📝 邮件列表

1. **[06-16 13:34]** Re: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-17 13:49]** Re: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

