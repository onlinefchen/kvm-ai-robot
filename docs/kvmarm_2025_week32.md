# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:29:31

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 310
- **总 Thread 数**: 29
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 28 threads (225 邮件)
- **RFC**: 1 threads (85 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 48 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  6 Aug 2025 12:56:22 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的一系列补丁，主要集中在对中介虚拟性能监控单元（mediated vPMU）的支持上。

1. **原始补丁内容**：补丁系列的主题是为 KVM x86 添加对中介 vPMU 的支持。中介 vPMU 允许虚拟机直接访问硬件性能监控计数器（PMCs），而不需要通过 KVM 进行仿真，从而提高性能。

2. **历史讨论要点**：之前的讨论主要集中在补丁的设计和实现细节上，包括如何处理 PMU 的上下文切换、事件选择器的管理，以及如何在虚拟机进入和退出时正确加载和保存 PMU 状态。补丁还涉及了对 Intel 和 AMD 处理器的特定要求。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的细节审查和测试结果上。参与者确认所有 PMU 相关的自测和 KUT 测试在 Intel Sapphire Rapids 上运行良好，没有发现问题。此外，补丁还引入了新的 API 来加载和保存中介 PMU 的上下文，确保在虚拟机运行时能够正确管理 PMU 状态。最后，补丁集被认为是良好的，准备进行更广泛的测试。

整体来看，这一系列补丁旨在优化 KVM 的性能监控能力，减少虚拟化开销，并确保在多种硬件平台上的兼容性和稳定性。

#### 📝 邮件列表

1. **[08-06 12:56]** [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-06 12:56]** [PATCH v5 01/44] perf: Skip pmu_ctx based on event_type
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-06 12:56]** [PATCH v5 02/44] perf: Add generic exclude_guest support
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-06 12:56]** [PATCH v5 03/44] perf: Move security_perf_event_free() call to __free_event()
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-06 12:56]** [PATCH v5 04/44] perf: Add APIs to create/release mediated guest vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-06 12:56]** [PATCH v5 05/44] perf: Clean up perf ctx time
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-06 12:56]** [PATCH v5 06/44] perf: Add a EVENT_GUEST flag
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[08-06 12:56]** [PATCH v5 07/44] perf: Add APIs to load/put guest mediated PMU context
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[08-06 12:56]** [PATCH v5 08/44] perf: core/x86: Register a new vector for handling
 mediated guest PMIs
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[08-06 12:56]** [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI vector
 on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[08-06 12:56]** [PATCH v5 10/44] perf/x86/core: Do not set bit width for unavailable counters
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[08-06 12:56]** [PATCH v5 11/44] perf/x86/core: Plumb mediated PMU capability from
 x86_pmu to x86_pmu_cap
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[08-06 12:56]** [PATCH v5 12/44] perf/x86/intel: Support PERF_PMU_CAP_MEDIATED_VPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[08-06 12:56]** [PATCH v5 13/44] perf/x86/amd: Support PERF_PMU_CAP_MEDIATED_VPMU for
 AMD host
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[08-06 12:56]** [PATCH v5 14/44] KVM: VMX: Setup canonical VMCS config prior to kvm_x86_vendor_init()
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[08-06 12:56]** [PATCH v5 15/44] KVM: SVM: Check pmu->version, not enable_pmu, when
 getting PMC MSRs
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[08-06 12:56]** [PATCH v5 16/44] KVM: Add a simplified wrapper for registering perf callbacks
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[08-06 12:56]** [PATCH v5 17/44] KVM: x86/pmu: Snapshot host (i.e. perf's) reported
 PMU capabilities
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[08-06 12:56]** [PATCH v5 18/44] KVM: x86/pmu: Start stubbing in mediated PMU support
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[08-06 12:56]** [PATCH v5 19/44] KVM: x86/pmu: Implement Intel mediated PMU
 requirements and constraints
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[08-06 12:56]** [PATCH v5 20/44] KVM: x86/pmu: Implement AMD mediated PMU requirements
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[08-06 12:56]** [PATCH v5 21/44] KVM: x86/pmu: Register PMI handler for mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[08-06 12:56]** [PATCH v5 22/44] KVM: x86: Rename vmx_vmentry/vmexit_ctrl() helpers
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[08-06 12:56]** [PATCH v5 23/44] KVM: x86/pmu: Move PMU_CAP_{FW_WRITES,LBR_FMT} into
 msr-index.h header
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[08-06 12:56]** [PATCH v5 24/44] KVM: x86: Rework KVM_REQ_MSR_FILTER_CHANGED into a
 generic RECALC_INTERCEPTS
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[08-06 12:56]** [PATCH v5 25/44] KVM: x86: Use KVM_REQ_RECALC_INTERCEPTS to react to
 CPUID updates
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[08-06 12:56]** [PATCH v5 26/44] KVM: VMX: Add helpers to toggle/change a bit in VMCS
 execution controls
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[08-06 12:56]** [PATCH v5 27/44] KVM: x86/pmu: Disable RDPMC interception for
 compatible mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[08-06 12:56]** [PATCH v5 28/44] KVM: x86/pmu: Load/save GLOBAL_CTRL via entry/exit
 fields for mediated PMU
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[08-06 12:56]** [PATCH v5 29/44] KVM: x86/pmu: Use BIT_ULL() instead of open coded equivalents
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[08-06 12:56]** [PATCH v5 30/44] KVM: x86/pmu: Move initialization of valid PMCs
 bitmask to common x86
   - 发件人: Sean Christopherson <seanjc@google.com>
32. **[08-06 12:56]** [PATCH v5 31/44] KVM: x86/pmu: Restrict GLOBAL_{CTRL,STATUS}, fixed
 PMCs, and PEBS to PMU v2+
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[08-06 12:56]** [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[08-06 12:56]** [PATCH v5 33/44] KVM: x86/pmu: Bypass perf checks when emulating
 mediated PMU counter accesses
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[08-06 12:56]** [PATCH v5 34/44] KVM: x86/pmu: Introduce eventsel_hw to prepare for
 pmu event filtering
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[08-06 12:56]** [PATCH v5 35/44] KVM: x86/pmu: Reprogram mediated PMU event selectors
 on event filter updates
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[08-06 12:56]** [PATCH v5 36/44] KVM: x86/pmu: Always stuff GuestOnly=1,HostOnly=0
 for mediated PMCs on AMD
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[08-06 12:56]** [PATCH v5 37/44] KVM: x86/pmu: Load/put mediated PMU context when
 entering/exiting guest
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[08-06 12:57]** [PATCH v5 38/44] KVM: x86/pmu: Disallow emulation in the fastpath if
 mediated PMCs are active
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[08-06 12:57]** [PATCH v5 39/44] KVM: x86/pmu: Handle emulated instruction for
 mediated vPMU
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[08-06 12:57]** [PATCH v5 40/44] KVM: nVMX: Add macros to simplify nested MSR
 interception setting
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[08-06 12:57]** [PATCH v5 41/44] KVM: nVMX: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[08-06 12:57]** [PATCH v5 42/44] KVM: nSVM: Disable PMU MSR interception as
 appropriate while running L2
   - 发件人: Sean Christopherson <seanjc@google.com>
44. **[08-06 12:57]** [PATCH v5 43/44] KVM: x86/pmu: Expose enable_mediated_pmu parameter
 to user space
   - 发件人: Sean Christopherson <seanjc@google.com>
45. **[08-06 12:57]** [PATCH v5 44/44] KVM: x86/pmu: Elide WRMSRs when loading guest PMCs
 if values already match
   - 发件人: Sean Christopherson <seanjc@google.com>
46. **[08-08 15:30]** Re: [PATCH v5 07/44] perf: Add APIs to load/put guest mediated PMU
 context
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
47. **[08-08 16:28]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
48. **[08-08 16:35]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>

---

### Thread 2: [PATCH 00/11] support SCTLR2_ELx

**📧 邮件数**: 19 | **👥 参与者**: 4 | **📅 开始时间**: Mon,  4 Aug 2025 13:17:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 Linux 内核的一个补丁系列，旨在支持 ARM 架构中的 SCTLR2_ELx 寄存器。该补丁系列包含 11 个补丁，主要内容是为 ARMv8.8/ARMv9.3 及更高版本的架构添加对 SCTLR2_ELx 寄存器的支持。这些寄存器的修改在当前版本的 Linux 中并非严格必要，但未来的架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要对这些寄存器进行配置。

在历史讨论中，补丁的初步版本已经被提出，讨论了如何在内核中实现这些寄存器的初始化、保存和恢复等功能。Yeoreum Yun 提到这些补丁基于 v6.16 版本，并表示尚未进行全面测试。

本周的新讨论中，参与者对补丁的具体实现进行了反馈。Mark Brown 建议在添加寄存器时引用相关规范的修订版本，以便于未来的更新。同时，Marc Zyngier 指出部分补丁可能是多余的，并建议在 6.17 版本发布后进行重基。Yeoreum Yun 表示将根据反馈进行修改和重基。

总体来看，本周的讨论集中在补丁的细节和未来的改进方向上，参与者对补丁的初步实现表示认可，同时也提出了需要进一步完善的地方。

#### 📝 邮件列表

1. **[08-04 13:17]** [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-04 13:17]** [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-04 13:17]** [PATCH 02/11] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[08-04 13:17]** [PATCH 03/11] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[08-04 13:17]** [PATCH 04/11] arm64: cpufeature: add FEAT_SCTLR2 feature
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[08-04 13:17]** [PATCH 05/11] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[08-04 13:17]** [PATCH 06/11] arm64: init SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[08-04 13:17]** [PATCH 07/11] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[08-04 13:17]** [PATCH 08/11] KVM: arm64: initialise SCTLR2_EL1 at __kvm_host_psci_cpu_entry()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[08-04 13:17]** [PATCH 09/11] KVM: arm64: support SCTLR2_EL1 for guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[08-04 13:17]** [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
12. **[08-04 13:17]** [PATCH 11/11] KVM: arm64: expose FEAT_SCTLR2 feature to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[08-04 13:24]** Re: [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[08-04 13:37]** Re: [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-04 14:04]** Re: [PATCH 00/11] support SCTLR2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[08-04 14:05]** Re: [PATCH 01/11] arm64/sysreg: add system registers SCTLR2_EL2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
17. **[08-04 14:11]** Re: [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[08-04 16:03]** Re: [PATCH 10/11] KVM: arm64: nv: support SCTLR2_ELx on nv
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
19. **[08-05 17:01]** Re: [PATCH 07/11] arm64: make the per-task SCTLR2_EL1
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 3: [PATCH kvmtool v3 0/6] arm64: Nested virtualization support

**📧 邮件数**: 16 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 10:57:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁（PATCH kvmtool v3 0/6）。该补丁系列的主要目标是为 KVM 工具添加对嵌套虚拟化的支持，确保在主线内核中实现的相关功能能够在 kvmtool 中得到应用。

在历史讨论中，补丁的内容包括更新内核头文件以支持新的 EL2 能力、允许用户通过命令行参数启动嵌套虚拟机、设置维护中断、控制全局计数器偏移、支持 FEAT_E2H0 以及生成 HYP 定时器中断说明符。讨论中提到，Marc 的努力使得 ARM64 的嵌套虚拟化支持已进入主线内核。

在本周的新讨论中，参与者 Alexandru Elisei 针对补丁提出了一些建议和问题，包括对命令行参数命名的清晰性、代码中的小错误、以及补丁实现的一些细节。Marc Zyngier 对这些建议进行了回应，强调了 KVM 的行为符合架构规范，并对某些实现细节进行了辩护。总体来看，本周的讨论集中在补丁的细节和实现一致性上，未达成明确的结论，但显示出对补丁质量的关注和进一步改进的意愿。

#### 📝 邮件列表

1. **[07-29 10:57]** [PATCH kvmtool v3 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[07-29 10:57]** [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[07-29 10:57]** [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[07-29 10:57]** [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[07-29 10:57]** [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[07-29 10:57]** [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[08-04 15:41]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[08-04 15:43]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting
 maintenance IRQ
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[08-04 15:45]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[08-04 15:45]** Re: [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[08-04 15:47]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt
 specifiers
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[08-04 18:45]** Re: [PATCH kvmtool v3 2/6] arm64: Initial nested virt support
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-04 18:51]** Re: [PATCH kvmtool v3 3/6] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[08-04 18:57]** Re: [PATCH kvmtool v3 4/6] arm64: add counter offset control
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-04 19:11]** Re: [PATCH kvmtool v3 5/6] arm64: add FEAT_E2H0 support
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[08-04 19:15]** Re: [PATCH kvmtool v3 6/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 08 Aug 2025 12:22:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE（Statistical Profiling Extension）特性的补丁集，主要集中在新增的过滤功能上。

1. **原始补丁内容**：该补丁集（[PATCH v6 00/12]）引入了三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性可以独立应用，涉及到多个补丁，分别处理系统寄存器的更改和性能工具的适配。

2. **历史讨论要点**：在之前的讨论中，补丁经历了多个版本的修改，主要集中在解决与其他更改的冲突、更新提交信息以及对功能的文档化等方面。补丁的目标是提高性能监控的灵活性和准确性。

3. **本周的新讨论与进展**：本周的讨论中，James Clark 提交了多个补丁，逐步实现了新特性的支持，包括对数据源过滤的支持（SPE_FEAT_FDS）和扩展过滤（FEAT_SPE_EFT）。补丁中还增加了新的 `config4` 字段以支持新的过滤功能，并更新了相关文档，详细描述了新特性的使用方法和注意事项。Leo Yan 对补丁进行了测试并确认其正常工作。此外，讨论中提到了一些小的修正和文档更新。

总体来看，本周的讨论和进展表明，针对 ARMv8.8 SPE 特性的补丁集正在稳步推进，相关功能的实现和文档化工作也在持续进行中。

#### 📝 邮件列表

1. **[08-08 12:22]** [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[08-08 12:22]** [PATCH v6 01/12] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[08-08 12:22]** [PATCH v6 02/12] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[08-08 12:23]** [PATCH v6 03/12] perf: arm_spe: Expose event filter
   - 发件人: James Clark <james.clark@linaro.org>
5. **[08-08 12:23]** [PATCH v6 04/12] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
6. **[08-08 12:23]** [PATCH v6 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
7. **[08-08 12:23]** [PATCH v6 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
8. **[08-08 12:23]** [PATCH v6 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
9. **[08-08 12:23]** [PATCH v6 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
10. **[08-08 12:23]** [PATCH v6 09/12] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
11. **[08-08 12:23]** [PATCH v6 10/12] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
12. **[08-08 12:23]** [PATCH v6 11/12] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
13. **[08-08 12:23]** [PATCH v6 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>
14. **[08-08 13:37]** Re: [PATCH v6 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: Leo Yan <leo.yan@arm.com>
15. **[08-08 13:39]** Re: [PATCH v6 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 5: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  5 Aug 2025 14:56:13 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM（Kernel-based Virtual Machine）在处理受保护虚拟机的受限寄存器时遇到的问题，主要集中在 arm64 架构上。Fuad Tabba 提出了一个包含四个补丁的系列，旨在解决 pKVM（保护虚拟机）中与受限寄存器访问和未定义异常注入相关的问题。

**原始补丁内容**：
补丁系列主要包括：
1. 处理 AIDR_EL1 和 REVIDR_EL1 寄存器的访问。
2. 使 vcpu_{read,write}_sys_reg 函数可用于 HYP 代码。
3. 在注入未定义异常时同步受保护虚拟机的 VBAR_EL1。
4. 修复 hVHE 模式下的访客字节序检查。

**之前讨论要点**：
在历史讨论中，未提及具体的补丁内容，但可以推测之前的讨论围绕着 pKVM 的实现细节和潜在问题展开。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现和潜在问题上。Fuad 提到，补丁 3 中的逻辑确保在注入异常前读取最新的 VBAR_EL1 值，以避免使用过时的值。Will Deacon 对补丁提出了一些建议，询问某些函数的适用性和代码的体积问题。最终，Fuad 表示将根据反馈进行修改，并在后续版本中修正补丁。整体来看，本周的讨论推动了补丁的进一步完善，确保了对 pKVM 的支持更加稳定和可靠。

#### 📝 邮件列表

1. **[08-05 14:56]** [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-05 14:56]** [PATCH v1 1/4] KVM: arm64: Handle AIDR_EL1 and REVIDR_EL1 in host for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-05 14:56]** [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg available
 to HYP code
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-05 14:56]** [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on injecting
 an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-05 14:56]** [PATCH v1 4/4] arm64: vgic-v2: Fix guest endianness check in hVHE mode
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[08-05 15:35]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Will Deacon <will@kernel.org>
7. **[08-05 15:38]** Re: [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg
 available to HYP code
   - 发件人: Will Deacon <will@kernel.org>
8. **[08-05 15:39]** Re: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted
 registers for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
9. **[08-05 16:20]** Re: [PATCH v1 0/4] KVM: arm64: Fixes to handling of restricted
 registers for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[08-05 16:25]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[08-05 16:51]** Re: [PATCH v1 2/4] KVM: arm64: Make vcpu_{read,write}_sys_reg
 available to HYP code
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[08-05 19:41]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on injecting an undef exception
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-05 19:43]** Re: [PATCH v1 3/4] KVM: arm64: Sync protected guest VBAR_EL1 on
 injecting an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 6: [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 17:52:47 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 pKVM 提供 SMMUv3 驱动的补丁（[PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM）。该补丁的主要目的是实现 DMA 隔离，支持 SMMUv3 的基本功能，且不依赖于树外的 pKVM 组件。

在历史讨论中，Mostafa Saleh 提出了补丁的初步版本，并针对 DMA 隔离的实现进行了详细说明。Jason Gunthorpe 对补丁提出了分拆建议，认为新 IOMMU 驱动的引入应作为独立补丁进行审查，并对 API 的设计提出了改进意见，强调了简洁性和清晰性的重要性。

在本周的新讨论中，Mostafa 和 Jason 继续探讨 SMMU 驱动的设计细节，Mostafa 表示可以考虑去掉 hypercalls 和 IOMMU ops，以简化补丁的复杂性，并提出将 pKVM 驱动与现有的 ARM_SMMU_V3 驱动合并的想法，以减少代码重复和复杂性。Jason 也支持这一思路，认为这样可以更好地支持未来的嵌套功能。

总体而言，本周的讨论集中在如何优化补丁设计和简化驱动结构，以便更有效地实现 SMMUv3 的支持。

#### 📝 邮件列表

1. **[07-28 17:52]** [PATCH v3 00/29] KVM: arm64: SMMUv3 driver for pKVM
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[07-28 17:53]** [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[07-30 11:42]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
4. **[07-30 15:07]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[07-30 13:47]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
6. **[07-31 14:17]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[07-31 13:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
8. **[07-31 17:44]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[08-01 15:59]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
10. **[08-04 14:41]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[08-05 14:57]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
12. **[08-06 14:10]** Re: [PATCH v3 29/29] iommu/arm-smmu-v3-kvm: Add IOMMU ops
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 7: [PATCH v2 0/5] KVM: arm64: FEAT_RASv1p1 support and RAS selection

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  6 Aug 2025 17:56:10 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FEAT_RASv1p1 的一系列补丁（patch）。补丁的主要内容包括添加对 RASv1p1 功能的支持、处理相关寄存器、以及确保在虚拟机迁移时的兼容性。

在历史讨论中，Marc Zyngier 提出了补丁系列的初始版本，并在此基础上进行了多次迭代，主要集中在如何正确处理 RASv1p1 寄存器以及在虚拟机中正确暴露该特性。补丁还解决了 RASv1p1 的复杂性，确保系统能够正确识别和处理该特性。

本周的新讨论中，Marc 提出了五个补丁的具体实现，包括：
1. 添加表示 FEAT_RASv1p1 的能力。
2. 处理 RASv1p1 寄存器。
3. 忽略由 L1 客户端的 EL2 设置的 HCR_EL2.FIEN。
4. 以标准方式暴露 FEAT_RASv1p1。
5. 使 ID_AA64PFR0_EL1.RAS 可写，以便在不同 RAS 支持的系统间迁移虚拟机。

参与者 Joey Gouly 和 Oliver Upton 对补丁进行了审查，并提出了一些担忧，尤其是关于在不同版本的 RASv1p1 之间迁移的潜在问题。Marc 也意识到需要对 RAS_frac 进行可写处理，以确保兼容性。整体来看，讨论集中在如何确保 KVM 在支持 RASv1p1 的同时，保持系统的稳定性和兼容性。

#### 📝 邮件列表

1. **[08-06 17:56]** [PATCH v2 0/5] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-06 17:56]** [PATCH v2 1/5] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[08-06 17:56]** [PATCH v2 2/5] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-06 17:56]** [PATCH v2 3/5] KVM: arm64: Ignore HCR_EL2.FIEN set by L1 guest's EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[08-06 17:56]** [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-06 17:56]** [PATCH v2 5/5] KVM: arm64: Make ID_AA64PFR0_EL1.RAS writable
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-07 12:12]** Re: [PATCH v2 2/5] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[08-07 13:55]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical
 manner
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[08-08 15:48]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical
 manner
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[08-09 21:19]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[08-09 21:21]** Re: [PATCH v2 4/5] KVM: arm64: Expose FEAT_RASv1p1 in a canonical manner
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 24 Jul 2025 23:51:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM (Kernel-based Virtual Machine) 在 arm64 架构下定期销毁二级页表的补丁。最初的补丁（PATCH 2/2）由 Raghavendra Rao Ananta 提出，目的是解决在突然销毁一个完全映射的 128G 虚拟机时出现的调度警告问题。该补丁通过分割销毁过程，允许在销毁大页表时进行 CPU 的调度，从而减少长时间占用 CPU 的风险。

在历史讨论中，Raghavendra 提出了将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个函数，以便在处理页表时可以在每个处理块之间调用 `cond_resched()`，以便让出 CPU。Oliver Upton 也指出，受保护模式可能会受到更严重的影响，建议在受保护和非受保护的流程中都使用 `stage2_destroy_range()`。

在本周的新讨论中，Raghavendra 反馈了在实际测试中发现的性能问题，指出在处理较小虚拟机时，销毁过程的时间显著增加，提出了将 `cond_resched()` 的调用移至实际解除映射的地方，以优化性能。Oliver 也对此进行了回应，提出了一些修复建议，以保持调度逻辑的一致性。

总体来看，本周的讨论集中在优化补丁的性能和实现细节上，参与者们积极探讨如何在不影响功能的前提下，提高代码的执行效率。

#### 📝 邮件列表

1. **[07-24 23:51]** [PATCH 0/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[07-24 23:51]** [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[07-24 23:51]** [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[07-29 09:01]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-07 11:58]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table periodically
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[08-08 11:56]** Re: [PATCH 2/2] KVM: arm64: Destroy the stage-2 page-table
 periodically
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[08-08 11:57]** Re: [PATCH 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[08-09 15:48]** [PATCH 0/2] KVM: arm64: AT + SR accessor fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-09 15:48]** [PATCH 1/2] KVM: arm64: nv: Fix ATS12 handling of single-stage translation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[08-09 15:48]** [PATCH 2/2] KVM: arm64: Fix vcpu_{read,write}_sys_reg() accessors
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v1 0/2] KVM: arm: nv: fix AT S* behaviour

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 6 Aug 2025 14:17:54 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 ARM 架构下的两个补丁，旨在修复 AT S* 指令的行为，特别是 S2 转换的问题。

**原始补丁内容**：
补丁主要包括两个部分：第一个补丁修复了 nVHE（非虚拟化扩展）客户机的 S2 转换，确保其能够正确获取 S2 转换结果；第二个补丁则更新了在执行 AT S* 指令后，CPU 寄存器 PAR_EL1 的值，以确保其反映最新的状态。

**之前讨论要点**：
在历史讨论中，参与者指出了 S2 转换在 VHE 嵌套虚拟机中的表现不一致，尤其是在处理 DomU 时，出现了错误的地址转换。补丁的提出是为了确保在所有情况下都能正确处理 S2 转换，避免因实现细节导致的偶然成功。

**本周新讨论进展**：
本周的讨论集中在补丁的细节上，参与者对补丁的逻辑进行了审查和修改建议。Oliver Upton 和 Marc Zyngier 提出了对补丁逻辑的改进意见，强调了 ARM 架构规范中对 S2 转换的要求。最终，Volodymyr Babchuk 表示将根据 Oliver 的建议进行修改，并计划提交最终补丁。整体来看，本周的讨论推动了补丁的完善，确保了对 ARM 架构的准确实现。

#### 📝 邮件列表

1. **[08-06 14:17]** [PATCH v1 0/2] KVM: arm: nv: fix AT S* behaviour
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
2. **[08-06 14:17]** [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after 'at
 s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
3. **[08-06 14:17]** [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
4. **[08-06 10:37]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-06 18:45]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-06 19:17]** Re: [PATCH v1 1/2] KVM: arm64: nv: fix S2 translation for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-06 11:40]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[08-06 19:56]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after 'at s*'
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-06 20:00]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
10. **[08-06 20:30]** Re: [PATCH v1 2/2] KVM: arm64: nv: update CPU register PAR_EL1 after
 'at s*'
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>

---

### Thread 10: [PATCH RFC v2 0/2] KVM: arm64: PMU: Use multiple host PMUs

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 06 Aug 2025 18:09:53 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 系统中如何使用多个主机 PMU（性能监控单元）的补丁。该补丁的核心是引入 `KVM_ARM_VCPU_PMU_V3_COMPOSITION` 属性，以便在异构系统中创建一个“复合” PMU，从而解决 vCPU 在迁移到不兼容的 pCPU 时计数器停止增量的问题。这一问题在 Windows 客户端中尤为明显，可能导致崩溃。

在历史讨论中，参与者提到当前的解决方案需要将 vCPU 固定到共享兼容 PMU 的 pCPU，这在 QEMU/libvirt 中实现起来非常复杂。新补丁允许 VMM（虚拟机监控器）在所有可用的 pCPU 上调度 vCPU，提高了主机硬件的利用率。

本周的讨论中，Akihiko Odaki 提出了补丁的具体实现和自测代码，Oliver Upton 则对补丁的规模表示担忧，建议将其拆分为更小的补丁以便于审查，并对补丁的设计和实现细节提出了一些建议和改进意见。最终，Odaki 表示将考虑 Upton 的建议，并继续完善补丁的实现。

#### 📝 邮件列表

1. **[08-06 18:09]** [PATCH RFC v2 0/2] KVM: arm64: PMU: Use multiple host PMUs
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
2. **[08-06 18:09]** [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
3. **[08-06 18:09]** [PATCH RFC v2 2/2] KVM: arm64: selftests: Test guest PMUv3
 composition
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
4. **[08-06 10:20]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[08-07 03:24]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
6. **[08-06 19:03]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[08-07 23:06]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>
8. **[08-08 16:08]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[08-09 15:15]** Re: [PATCH RFC v2 1/2] KVM: arm64: PMU: Introduce
 KVM_ARM_VCPU_PMU_V3_COMPOSITION
   - 发件人: Akihiko Odaki <odaki@rsg.ci.i.u-tokyo.ac.jp>

---

### Thread 11: [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 09 Aug 2025 02:33:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）1.2 版本的补丁集（PATCH v10 0/6）。该补丁集的主要内容是引入新的 SEND_DIRECT2 ABI，允许使用更多寄存器（x4-x17）作为消息负载，并确保主机不会使用低于已协商版本的 FF-A 版本。

在历史讨论中，补丁的演变过程被详细记录，包括对先前版本的修改和更新。补丁集的目标是为超管提供对 FF-A 1.2 的支持，以便实现新的 FFA_MSG_SEND_DIRECT_REQ2 消息接口，并更新所有 SMC 调用以使用 SMCCC 1.2，从而简化接口支持。

本周的新讨论中，参与者 Per Larsen 提出了多个具体补丁，包括：
1. 修正主机版本降级尝试的返回值，确保协商后的版本保持锁定。
2. 在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2，以支持更多返回值。
3. 将 FFA_NOTIFICATION_* 接口标记为不支持，防止其被传递到可信执行环境（TZ）。
4. 将 FF-A 1.2 的可选接口标记为不支持，以防止被代理。
5. 在 FFA_FEATURE 调用中屏蔽响应，确保返回的最小缓冲区大小正确。
6. 将支持的 FF-A 版本提升到 1.2，以启用新的消息接口。

这些补丁得到了 Will Deacon 的认可，表明了社区对这一进展的支持。整体来看，这些讨论和补丁的提交旨在增强 KVM 在 arm64 上的功能和兼容性。

#### 📝 邮件列表

1. **[08-09 02:33]** [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[08-09 02:33]** [PATCH v10 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[08-09 02:33]** [PATCH v10 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[08-09 02:33]** [PATCH v10 3/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[08-09 02:33]** [PATCH v10 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[08-09 02:33]** [PATCH v10 5/6] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[08-09 02:33]** [PATCH v10 6/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 12: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Sat,  2 Aug 2025 18:40:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的页表转储（ptdump）功能的修复，具体是修复可执行属性的打印错误。原始的补丁由 Wei-Lin Chang 提出，指出当前的实现错误地将不可执行区域标记为 "X"，而可执行区域则为空格，原因在于打印字符串的判断错误。补丁的目的是通过交换这两个字符串来解决这个问题。

在历史讨论中，Anshuman Khandual 提出了对补丁的质疑，认为 KVM_PTE_LEAF_ATTR_HI_S2_XN 宏的语义与预期相反，导致了打印错误。

在本周的新讨论中，Wei-Lin Chang 针对 Anshuman 的反馈进行了详细分析，确认了当前代码逻辑的问题。Mark Rutland 提出，PTE_VALID 位不应包含在掩码中，并建议将其作为单独的过滤器来处理。Anshuman 和 Sebastian Ene 也支持这一观点，认为在现有过滤器中检查 PTE_VALID 是不合理的。最终，Wei-Lin Chang 表示会根据大家的反馈进行修正，并准备提交补丁的第二版（v2）。

总结而言，本周的讨论集中在如何正确处理 PTE_VALID 位的问题上，参与者们一致认为需要调整现有的过滤器逻辑，以确保输出与 Stage-1 页表转储一致。

#### 📝 邮件列表

1. **[08-02 18:40]** [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-03 19:33]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[08-04 20:41]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[08-04 16:22]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[08-05 05:10]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[08-05 08:31]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Sebastian Ene <sebastianene@google.com>
7. **[08-07 11:12]** Re: [PATCH] KVM: arm64: ptdump: Fix exec attribute printing
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 13: [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 13:00:05 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM（Protected KVM）虚拟机处理。历史讨论中，Fuad Tabba 提出了一个补丁系列，主要是为了在虚拟机初始化时保留 pKVM 的 VM 句柄，这个句柄用于在主机内核和虚拟机监控器之间唯一标识虚拟机。补丁中还包括将 `pkvm.enabled` 字段重命名为 `pkvm.is_protected`，以消除对虚拟机状态的混淆。

在之前的讨论中，Wei-Lin Chang 提出了对 pKVM 代码的理解问题，并询问是否会在未来允许用户选择启动受保护的虚拟机。Fuad 确认了正在进行的 pKVM 上游工作，特别是对受保护虚拟机的支持，并提到 Android 中已有相关实现。

本周的新讨论中，Fuad 进一步解释了他们希望上游的内容，包括在创建虚拟机时指定其为受保护类型，并将 `is_protected` 设置为 true。Wei-Lin 对此表示感谢并确认理解。Kunwu Chan 也对补丁进行了审核并表示认可。这表明该补丁系列在社区中获得了积极的反馈和支持。

#### 📝 邮件列表

1. **[07-29 13:00]** [PATCH v1 0/8] KVM: arm64: Reserve pKVM VM handle during initial VM setup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[07-29 13:00]** [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-03 14:10]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[08-04 08:00]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to pkvm.is_protected
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-04 20:20]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
6. **[08-08 19:32]** Re: [PATCH v1 1/8] KVM: arm64: Rename pkvm.enabled to
 pkvm.is_protected
   - 发件人: Kunwu Chan <kunwu.chan@linux.dev>

---

### Thread 14: [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  7 Aug 2025 13:01:30 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理受限寄存器的修复补丁。这一系列补丁主要解决了在受保护虚拟机（pKVM）中遇到的与受限寄存器访问和注入未定义异常相关的问题。

历史讨论部分没有提供具体的背景信息，但本周的新讨论中，Fuad Tabba 提交了三条补丁。第一条补丁处理了 AIDR_EL1 和 REVIDR_EL1 寄存器的访问问题，确保在受保护虚拟机中，主机能够正确处理这些寄存器的访问。第二条补丁解决了在注入未定义异常时可能出现的竞争条件，确保在异常处理时使用最新的 VBAR_EL1 值。第三条补丁修复了在 hVHE 模式下对来宾的字节序检查，确保访问的是来宾的 SCTLR_EL1 寄存器。

本周的讨论进展显示，这些补丁已被 Oliver Upton 应用到修复集中，标志着这些问题的解决。整体来看，这些补丁增强了 KVM 在处理受保护虚拟机时的稳定性和可靠性。

#### 📝 邮件列表

1. **[08-07 13:01]** [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-07 13:01]** [PATCH v2 1/3] KVM: arm64: Handle AIDR_EL1 and REVIDR_EL1 in host for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-07 13:01]** [PATCH v2 2/3] KVM: arm64: Sync protected guest VBAR_EL1 on injecting
 an undef exception
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[08-07 13:01]** [PATCH v2 3/3] arm64: vgic-v2: Fix guest endianness check in hVHE mode
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[08-08 10:51]** Re: [PATCH v2 0/3] KVM: arm64: Fixes to handling of restricted registers for protected VMs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 15: [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 21:15:03 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 规范的补丁集（PATCH v9 0/6）。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁的主要目的是防止主机使用低于已与虚拟机监控器协商的 FF-A 版本，因为虚拟机监控器缺乏必要的兼容路径来进行版本转换。

在历史讨论中，Per Larsen 提出了多个补丁，分别针对 FF-A 1.2 的初始化、使用 SMCCC 1.2 以及将某些 FF-A 1.2 接口标记为不支持。这些补丁的目的是确保在实现 FF-A 特性时的兼容性和简化代码。

在本周的新讨论中，Will Deacon 对 Per Larsen 提出的补丁进行了反馈，支持无条件使用 SMCCC 1.2，并指出检查函数 ID 不是正确的方法。他还对将 FF-A 1.2 接口标记为不支持的补丁表示认可，并询问安全侧是否应该拒绝相关请求。整体来看，本周的讨论进一步确认了补丁的方向和实现细节。

#### 📝 邮件列表

1. **[07-30 21:15]** [PATCH v9 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[07-30 21:15]** [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[07-30 21:15]** [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[08-08 13:39]** Re: [PATCH v9 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Will Deacon <will@kernel.org>
5. **[08-08 13:41]** Re: [PATCH v9 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 16: [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 29 Jul 2025 12:33:35 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主要关注于移除 `vm_dead` 状态并转而依赖 `vm_bugged` 来处理 -EIO 错误。Sean Christopherson 提出的补丁旨在解决当前对 `vm_dead` 的检查存在的竞争条件问题，这种检查没有锁保护，可能导致错误的安全感。补丁的核心是通过仅依赖 `vm_bugged` 来拒绝 ioctls，从而限制内核或硬件错误带来的损害。

在之前的讨论中，Adrian Hunter 提出了对补丁的担忧，认为移除 `vm_dead` 检查可能导致在已死亡的虚拟机中创建和运行 vCPUs，这显然是不理想的。他建议保留 `vm_dead` 检查，以防止潜在的问题，并提出了一些代码修改建议。

在本周的新讨论中，Chao Gao 对补丁表示支持，并建议在 `tdx_sept_remove_private_spte()` 函数中添加注释，以明确 `!is_hkid_assigned()` 表示来宾已终止，从而允许直接回收私有页面。整体来看，讨论在补丁的有效性和潜在风险之间达成了一定的共识。

#### 📝 邮件列表

1. **[07-29 12:33]** [PATCH 0/5] KVM: Drop vm_dead, pivot on vm_bugged for -EIO
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 12:33]** [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-01 16:56]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Adrian Hunter <adrian.hunter@intel.com>
4. **[08-01 09:44]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-06 14:06]** Re: [PATCH 5/5] KVM: TDX: Add sub-ioctl KVM_TDX_TERMINATE_VM
   - 发件人: Chao Gao <chao.gao@intel.com>

---

### Thread 17: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  7 Aug 2025 09:21:28 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个针对 Linux 内核 KVM（虚拟机监控器）在 ARM64 架构下的补丁，主题为将 `BUG_ON(1)` 替换为 `BUG()`。该补丁的目的是简化代码并避免在使用 Clang 编译器时出现误警告，尤其是在控制流分析中引发的未初始化变量警告。

在历史讨论中，补丁的背景并未详细说明，但可以推测出之前有关于 `BUG_ON()` 复杂性及其对编译器分析影响的讨论。Arnd Bergmann 提出了这一补丁，并指出 `BUG_ON()` 的使用增加了不必要的复杂性，可能导致编译器误报。

在本周的新讨论中，Nathan Chancellor 对补丁进行了审核并表示支持，确认了之前的构建报告问题。Oliver Upton 则表示该补丁已被应用到修复列表中，确认了补丁的有效性和重要性。

总的来说，本周的讨论表明该补丁得到了积极的反馈并已成功合并，解决了编译器警告问题，简化了代码逻辑。

#### 📝 邮件列表

1. **[08-07 09:21]** [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Arnd Bergmann <arnd@kernel.org>
2. **[08-07 08:56]** Re: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Nathan Chancellor <nathan@kernel.org>
3. **[08-08 10:51]** Re: [PATCH] kvm: arm64: use BUG() instead of BUG_ON(1)
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 18: [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 14:04:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE（可扩展性能监控）特性的补丁集，主要由 James Clark 提出。补丁集包含 12 个部分，支持三项新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性是独立的，可以分别应用。补丁的前两项特性与旧版 Perf 工具兼容，但最后一项特性需要对 Perf 工具进行修改以解析新的配置。

在历史讨论中，James Clark 提到了一些必要的系统寄存器更改及各个特性的补丁分布，并在第二封邮件中提出了一个补丁，旨在提取一个宏以检查 SPE 版本，提升代码可读性，并无功能性变化。

在本周的新讨论中，Leo Yan 对 James Clark 提出的补丁进行了反馈，指出他在主线内核上应用该补丁时遇到问题，原因是本地树缺少一个特定的提交（ae344bcb0d49），该提交更新了 __init_el2_fgt，因此建议 James 更新补丁以解决该问题。

#### 📝 邮件列表

1. **[07-21 14:04]** [PATCH v5 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[07-21 14:04]** [PATCH v5 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
3. **[08-08 10:18]** Re: [PATCH v5 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 19: [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 29 Jul 2025 15:54:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主题为“启用 mmap() 对于 guest_memfd 的支持”。该补丁的主要目的是为不使用 KVM_MEMORY_ATTRIBUTE_PRIVATE 的虚拟机类型添加主机用户空间对 guest_memfd 支持的内存映射功能。

在历史讨论中，Sean Christopherson 提到 arm64 的补丁已获得 Marc 的审核，x86 方面也准备就绪，只需 Paolo 的批准即可。补丁的实施将有助于解决与正在进行的系列之间的语义冲突。此外，补丁中还包括了对 guest_memfd 的自测试扩展，旨在验证 mmap 操作的成功性、数据完整性以及与 fallocate 的交互。

在本周的新讨论中，Shivank Garg 对补丁进行了审核并表示支持，确认了补丁的有效性。这表明该补丁在社区中获得了进一步的认可，预计将很快进入 kvm/next 分支。整体来看，该补丁的推进标志着 KVM 在内存管理方面的持续改进。

#### 📝 邮件列表

1. **[07-29 15:54]** [PATCH v17 00/24] KVM: Enable mmap() for guest_memfd
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[07-29 15:54]** [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when mmap
 is supported
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-07 13:42]** Re: [PATCH v17 23/24] KVM: selftests: guest_memfd mmap() test when
 mmap is supported
   - 发件人: Shivank Garg <shivankg@amd.com>

---

### Thread 20: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 21 Jul 2025 16:51:36 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加一个独立的自测试，以检查 KVM 的 UUID。Marc Zyngier 提出了一个补丁，目的是在 UUID 出现问题时能够及早发现，并通过自测试发出警告。补丁中包含了对相关文件的修改，增加了新的测试代码。

在之前的讨论中，Andrew Jones 对补丁提出了建议，询问是否应该检查返回值 `res.a0` 是否等于 `SMCCC_RET_SUCCESS`。他还提到这个模式在 KVM 中变得越来越常见，可能需要一个 ucall 辅助函数来简化操作。

在本周的新讨论中，Marc Zyngier 回复了 Andrew Jones，表示由于延迟回复，现在意识到之前的检查并不适用，因为 A0-A3 包含完整的 UID。虽然检查 A0 是否不等于 NOT_SUPPORTED 是有效的，但检查 A0 是否等于 SUCCESS 在 KVM 中并不适用，因此他决定删除这一断言，认为这一检查是没有意义的。

#### 📝 邮件列表

1. **[07-21 16:51]** [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[07-22 11:18]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for
 KVM's own UUID
   - 发件人: Andrew Jones <ajones@ventanamicro.com>
3. **[08-06 18:10]** Re: [PATCH] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 31 Jul 2025 20:58:41 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理虚拟机中的同步外部中止（SEA）时的改进，具体通过补丁 [PATCH v3 0/3] 来实现。

1. **原始问题**：当前，当主机的 APEI（ACPI Platform Error Interface）无法处理虚拟机中的同步外部中止时，KVM 会直接向虚拟 CPU 注入异步 SError，这通常导致虚拟机内核崩溃。尤其是在虚拟 CPU 遇到可恢复的未更正内存错误（UER）时，这种情况比较常见，可能会导致虚拟机重启后重新使用已损坏的内存。

2. **之前讨论要点**：在历史邮件中，Jiaqi Yan 提出了补丁的背景，强调了处理 SEA 的必要性，并描述了当前处理方式的缺陷。补丁的目标是通过让 KVM 在处理 SEA 时能够退出到用户空间，从而避免直接注入 SError，减少虚拟机崩溃的风险。

3. **本周的新讨论**：在本周的邮件中，Jiaqi Yan 对补丁进行了友好的提醒，寻求评审意见。这表明补丁已提交待审，但尚未收到反馈，开发者希望尽快推进该补丁的审查过程。

总体来看，本次讨论聚焦于改进 KVM 对 SEA 的处理方式，以提高虚拟机的稳定性和可靠性。

#### 📝 邮件列表

1. **[07-31 20:58]** [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[07-31 20:58]** [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[08-06 08:03]** Re: [PATCH v3 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 22: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Jul 2025 11:23:42 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理由于 VNCR（Virtual Non-Cacheable Region）重定向引起的 SEAs（Synchronous External Aborts）的补丁。

1. **原始 patch/问题的内容**：Oliver Upton 提出的补丁旨在处理系统寄存器访问被重定向到 VNCR 页面时可能产生的外部中止。补丁的核心是将这些外部中止路由到 `kvm_handle_guest_sea()` 函数，以便进行潜在的 APEI（ACPI Platform Error Interface）处理，如果内核未能处理该中止，则回退到 vSError。

2. **之前的讨论要点**：在历史讨论中，Oliver Upton 还提到将删除一个无用的头文件 `kvm_ras.h`，该文件只提供了一个单一的调用点，显示出对代码整洁性的关注。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Oliver Upton 表示该补丁已被应用于修复集，并感谢参与者的贡献。这表明补丁已成功整合进代码库，标志着该问题的解决。

整体来看，本次讨论集中在 KVM 对 arm64 架构下 VNCR 重定向引起的外部中止的处理上，补丁已成功应用并得到认可。

#### 📝 邮件列表

1. **[07-29 11:23]** [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[08-08 10:51]** Re: [PATCH] KVM: arm64: nv: Handle SEAs due to VNCR redirection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  6 Aug 2025 18:13:41 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试功能，主要是增加一个独立的测试用例，用于检查 KVM 的 UUID（通用唯一标识符）。

**原始 patch/问题的内容**：
Marc Zyngier 提出了一个补丁（PATCH v2），目的是添加一个自测试功能，以便在 KVM 的 UUID 被篡改时能够及时发现。补丁中包含了一个新的测试文件 `kvm-uuid.c`，该文件实现了对 KVM UUID 的检查。

**之前讨论要点**：
在历史讨论中没有相关的内容，因此没有额外的背景信息。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc Zyngier 提交的补丁得到了 Oliver Upton 的认可，并已被应用到修复列表中。这表明该补丁已成功集成，能够增强 KVM 的稳定性和安全性，确保 UUID 的完整性。补丁的具体提交链接也被提供，便于后续查阅。

#### 📝 邮件列表

1. **[08-06 18:13]** [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-08 10:51]** Re: [PATCH v2] KVM: arm64: selftest: Add standalone test checking for KVM's own UUID
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 24: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Jul 2025 11:18:28 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 VNCR_EL2 相关故障的补丁。历史讨论中，Marc Zyngier 提出了一个补丁，旨在修正对 ESR_EL2.VNCR 位的检查，指出之前的实现错误地测试了 ESR_EL2.DFSC 中的随机位，导致在处理权限和翻译故障时未能正确识别问题。他建议将 BUG_ON() 更改为 WARN_ON_ONCE()，以避免在此处崩溃。

在本周的新讨论中，Oliver Upton 确认已将该补丁应用于修复列表，并表示感谢。这表明补丁得到了认可并已被纳入代码库中，解决了之前提到的问题。

总结而言，此次讨论围绕 KVM 在处理特定故障时的代码修正，历史讨论提供了补丁的背景和必要性，而本周的进展则确认了补丁的应用和实施。

#### 📝 邮件列表

1. **[07-30 11:18]** [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-08 10:51]** Re: [PATCH] KVM: arm64: nv: Properly check ESR_EL2.VNCR on taking a VNCR_EL2 related fault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Jul 2025 14:07:36 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 Linux 内核 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在解决 Clang 编译器发出的关于未初始化常量指针的警告。

**原始 patch/问题的内容**：
补丁的主要目的是禁用 Clang 22 中出现的一个警告，该警告指出在调用 `get_clidr_el1()` 函数时，传递的 `clidr` 变量是一个未初始化的常量指针。尽管该函数实际上不在意指针的常量性，但编译器的警告仍然被视为一个误报。

**之前讨论要点**：
在历史讨论中，Justin Stitt 提出了补丁的背景，详细解释了警告的来源及其影响，强调了这是一个误报，并建议通过禁用该警告来解决问题。

**本周的新讨论、进展或结论**：
在本周的讨论中，参与者 Nathan Chancellor 对补丁表示认可，认为这是一个适当的解决方案，并给予了“审核通过”（Reviewed-by）的反馈。这表明补丁得到了积极的评审，可能会在未来的稳定版本中被采纳。

#### 📝 邮件列表

1. **[07-28 14:07]** [PATCH 6.1.y] KVM: arm64: sys_regs: disable -Wuninitialized-const-pointer
 warning
   - 发件人: Justin Stitt <justinstitt@google.com>
2. **[08-06 15:25]** Re: [PATCH 6.1.y] KVM: arm64: sys_regs: disable
 -Wuninitialized-const-pointer warning
   - 发件人: Nathan Chancellor <nathan@kernel.org>

---

### Thread 26: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 31 Jul 2025 08:56:59 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中支持 FF-A（Firmware Framework for Arm）版本的更新，具体是将支持的版本提升至 1.2。

**原始 patch/问题内容**：
该 patch 的目的是更新 KVM 对 FF-A 的支持版本，以便更好地兼容新版本的固件框架，确保虚拟化环境的稳定性和功能性。

**之前讨论要点**：
在历史讨论中，Marc Zyngier 提到，尽管有频繁的版本更新，但在未明确确认版本 1.2 及之前版本的相关内容时，不能轻易做出假设。他强调需要严格遵循 MBZ（Must Be Zero）原则，以避免未来版本中可能出现的解析问题。

**本周的新讨论、进展或结论**：
在本周的讨论中，Will Deacon 进一步澄清了之前的讨论内容。他指出，当前已协商出一个已知的 FF-A 版本，因此不必担心版本 1.337 的潜在问题。同时，他提到从 TZ（TrustZone）返回的响应中，如果 MBZ 位非零，建议忽略这些位。这一讨论有助于明确如何处理 FF-A 版本更新过程中的细节问题，并确保 KVM 的稳定性。

#### 📝 邮件列表

1. **[07-31 08:56]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-05 15:49]** Re: [PATCH v7 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 27: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 10 Aug 2025 21:12:22 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Clang 堆栈深度跟踪的补丁系列（PATCH v3 00/13），主要涉及对 Linux 内核中堆栈泄漏（stackleak）机制的改进。

在历史讨论中，补丁系列的具体内容并未详细列出，但可以推测这些补丁旨在增强堆栈安全性，特别是通过 Clang 工具链来跟踪堆栈深度，以防止潜在的堆栈泄漏问题。

本周的新讨论中，Kees Cook 确认了该补丁系列已被应用到 riscv/linux.git 的修复分支中。邮件中列出了补丁的具体内容，包括对堆栈泄漏相关功能的重命名、对不同架构（如 x86、arm、arm64、s390、powerpc 和 mips）处理 KCOV 的不匹配情况，以及对初始化相关的配置进行调整等。补丁的最后几项还涉及启用堆栈擦除和初始化时的默认配置。

总的来说，本周的进展表明该补丁系列已成功整合到代码库中，标志着对堆栈安全性增强的进一步推进。

#### 📝 邮件列表

1. **[08-10 21:12]** Re: [PATCH v3 00/13] stackleak: Support Clang stack depth tracking
   - 发件人: patchwork-bot+linux-riscv@kernel.org

---

### Thread 28: [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat,  9 Aug 2025 21:53:56 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 ptdump 功能的一个补丁（patch）。该补丁的主要内容是移除在测试属性时对 PTE_VALID 的检查，以避免与其他属性（如 R、W、X 和 AF）混淆，导致输出结果不准确。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出之前的讨论集中在 ptdump 代码中属性掩码和测试值的设计上，特别是如何正确地处理和显示可执行属性的问题。

在本周的新讨论中，Wei-Lin Chang 提出了补丁的具体实现，主要修改包括：从所有属性掩码和测试值中移除 PTE_VALID，以确保每个测试仅匹配相关位。此外，还更新了可执行属性的输出格式，使其与 stage-1 ptdump 保持一致，非可执行区域显示为 "NX"，可执行区域显示为 "x "。补丁经过测试并已提交，得到了多位开发者的建议和支持。

#### 📝 邮件列表

1. **[08-09 21:53]** [PATCH v2] KVM: arm64: ptdump: Don't test PTE_VALID alongside other attributes
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v1 00/38] ARM CCA Device Assignment support

**📧 邮件数**: 85 | **👥 参与者**: 10 | **📅 开始时间**: Mon, 28 Jul 2025 19:21:37 +0530

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM CCA（可信计算架构）设备分配支持的补丁系列（RFC PATCH v1 00/38）。该补丁旨在实现 ARM CCA 架构下的设备分配，基于 Alp12 规范进行代码修改，扩展了 TSM（可信安全管理）框架，使其在主机和客户机中均可使用。

在历史讨论中，Aneesh Kumar K.V 提出了多个补丁，涉及 DMA 分配、设备通信、物理设备的创建与销毁等功能，并讨论了如何处理安全设备的 DMA 访问和内存分配问题。参与者们对补丁的设计、实现细节和潜在问题进行了深入的技术讨论。

本周的新讨论中，参与者们对补丁进行了进一步的审查和反馈。例如，Aneesh 针对 Jonathan Cameron 的建议表示将更新补丁以包含所建议的更改。此外，讨论还涉及了如何处理 DMA 映射、设备状态管理以及在不同情况下的错误处理等问题。Jason Gunthorpe 和其他参与者对补丁的设计提出了具体的改进建议，并探讨了在 ARM 和 AMD 平台上的实现差异。

总体而言，本周的讨论集中在补丁的细节修改、功能实现的合理性以及如何确保补丁在不同硬件平台上的兼容性和有效性。

#### 📝 邮件列表

1. **[07-28 19:21]** [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[07-28 19:21]** [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[07-28 19:21]** [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private memory
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[07-28 19:21]** [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[07-28 19:21]** [RFC PATCH v1 06/38] iommufd: Add and option to request for bar mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[07-28 19:21]** [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[07-28 19:21]** [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[07-28 19:21]** [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[07-28 19:21]** [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[07-28 19:21]** [RFC PATCH v1 14/38] coco: host: arm64: Device communication support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[07-28 19:21]** [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the physical device
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[07-28 19:21]** [RFC PATCH v1 18/38] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[07-28 19:21]** [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[07-28 19:21]** [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual device communication
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
15. **[07-28 19:22]** [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
16. **[07-28 19:22]** [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest initiated TDI bind/unbind
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
17. **[07-28 19:22]** [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range found in the interface report
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
18. **[07-28 19:22]** [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start and stop support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
19. **[07-28 19:22]** [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create parameters
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
20. **[07-28 19:22]** [RFC PATCH v1 37/38] coco: guest: arm64: Add support for fetching device measurements
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
21. **[07-28 19:22]** [RFC PATCH v1 38/38] coco: guest: arm64: Add support for fetching device info
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
22. **[07-28 11:08]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
23. **[07-28 11:17]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
24. **[07-28 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
25. **[07-29 13:53]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
26. **[07-29 13:58]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
27. **[07-29 11:29]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
28. **[07-29 11:33]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
29. **[07-30 14:55]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
30. **[07-30 14:52]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
31. **[07-30 14:57]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
32. **[07-30 15:08]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
33. **[07-30 15:13]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
34. **[07-30 15:26]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
35. **[07-31 11:36]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
36. **[07-31 14:39]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
37. **[07-31 09:22]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
38. **[07-31 19:07]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
39. **[08-01 12:51]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
40. **[08-01 14:19]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
41. **[08-02 14:14]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
42. **[08-02 10:41]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
43. **[08-04 08:02]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
44. **[08-04 09:47]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
45. **[08-04 09:52]** Re: [RFC PATCH v1 15/38] coco: host: arm64: Stop and destroy the
 physical device
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
46. **[08-04 09:59]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
47. **[08-04 10:15]** Re: [RFC PATCH v1 21/38] coco: host: arm64: Add support for virtual
 device communication
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
48. **[08-04 10:20]** Re: [RFC PATCH v1 24/38] arm64: CCA: Register guest tsm callback
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
49. **[08-04 12:07]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
50. **[08-04 12:18]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
51. **[08-04 12:28]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
52. **[08-04 11:27]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Arto Merilainen <amerilainen@nvidia.com>
53. **[08-04 13:58]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
54. **[08-04 11:23]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Jonathan Cameron <Jonathan.Cameron@huawei.com>
55. **[08-04 16:52]** Re: [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
56. **[08-04 16:54]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
57. **[08-04 17:00]** Re: [RFC PATCH v1 05/38] tsm: Don't overload connect
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
58. **[08-04 17:03]** Re: [RFC PATCH v1 09/38] iommufd/vdevice: Add TSM Guest request uAPI
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
59. **[08-04 17:25]** Re: [RFC PATCH v1 08/38] iommufd/tsm: Add tsm_op iommufd ioctls
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
60. **[08-04 17:26]** Re: [RFC PATCH v1 19/38] coco: host: arm64: set_pubkey support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
61. **[08-04 17:27]** Re: [RFC PATCH v1 37/38] coco: guest: arm64: Add support for
 fetching device measurements
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
62. **[08-04 17:27]** Re: [RFC PATCH v1 35/38] coco: guest: arm64: Add Realm device start
 and stop support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
63. **[08-04 17:27]** Re: [RFC PATCH v1 18/38] X.509: Move certificate length retrieval
 into new helper
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
64. **[08-04 17:28]** Re: [RFC PATCH v1 13/38] coco: host: arm64: Create a PDEV with rmm
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
65. **[08-04 17:28]** Re: [RFC PATCH v1 32/38] coco: guest: arm64: Add support for guest
 initiated TDI bind/unbind
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
66. **[08-04 17:29]** Re: [RFC PATCH v1 14/38] coco: host: arm64: Device communication
 support
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
67. **[08-04 17:31]** Re: [RFC PATCH v1 34/38] coco: guest: arm64: Validate mmio range
 found in the interface report
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
68. **[08-04 17:31]** Re: [RFC PATCH v1 36/38] KVM: arm64: CCA: enable DA in realm create
 parameters
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
69. **[08-05 11:29]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
70. **[08-05 10:26]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Xu Yilun <yilun.xu@linux.intel.com>
71. **[08-05 10:20]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
72. **[08-05 10:37]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
73. **[08-05 14:54]** Re: [RFC PATCH v1 03/38] tsm: Move dsm_dev from pci_tdi to pci_tsm
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
74. **[08-05 20:22]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Alexey Kardashevskiy <aik@amd.com>
75. **[08-05 12:48]** Re: [RFC PATCH v1 10/38] iommufd/vdevice: Add TSM map ioctl
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
76. **[08-05 12:54]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
77. **[08-05 13:08]** Re: [RFC PATCH v1 04/38] tsm: Support DMA Allocation from private
 memory
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
78. **[08-05 13:10]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
79. **[08-05 14:27]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
80. **[08-05 11:27]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
81. **[08-05 15:42]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
82. **[08-05 12:06]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
83. **[08-05 16:38]** Re: [RFC PATCH v1 00/38] ARM CCA Device Assignment support
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
84. **[08-06 14:18]** Re: [RFC PATCH v1 06/38] iommufd: Add and option to request for bar
 mapping with IORESOURCE_EXCLUSIVE
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
85. **[08-08 23:37]** Re: [RFC PATCH v1 38/38] coco: guest: arm64: Add support for
 fetching device info
   - 发件人: Eric Biggers <ebiggers@kernel.org>

---

