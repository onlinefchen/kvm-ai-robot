# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 09:14:09

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 197
- **总 Thread 数**: 30
- **大型 Thread** (>20封): 1 个

### 分类分布

- **PATCH**: 22 threads (165 邮件)
- **RFC**: 4 threads (14 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Discussion**: 1 threads (4 邮件)
- **Other**: 2 threads (13 邮件)

---

## 📌 PATCH

共 22 个 thread

---

### Thread 1: [PATCH v2 00/14] KVM: arm64: Support FEAT_PMUv3 on Apple hardware

**📧 邮件数**: 35 | **👥 参与者**: 5 | **📅 开始时间**: Mon,  3 Feb 2025 10:30:57 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 Apple 硬件的 KVM (Kernel-based Virtual Machine) 的 PMUv3（性能监控单元版本3）支持的补丁系列。该补丁旨在增强 KVM 在 arm64 架构上的虚拟化能力，特别是在 Apple 的 M 系列芯片上。

### 原始补丁内容
补丁系列的核心是支持在 Apple 硬件上进行 PMUv3 的仿真，补丁包括对性能事件选择和过滤配置的重构、提供 PMUv3 事件的映射助手，以及在 KVM 中使用 cpucap 来判断系统是否支持 PMUv3。

### 之前讨论要点
历史讨论中，参与者主要集中在补丁的实现细节上，包括如何处理 Apple M 系列芯片的特定限制，以及如何确保补丁在不同配置下的兼容性。补丁的初步版本已经在 M2 Pro Mac Mini 上进行了测试，并且解决了一些编译错误。

### 本周新讨论与进展
本周的讨论中，Marc Zyngier 提出了对补丁的多项改进建议，包括对事件映射的逻辑进行优化，确保在无法翻译事件时不安装该事件。此外，讨论还涉及到如何处理新引入的 CPU 特性标志，以支持更复杂的虚拟化场景。参与者对补丁的整体方向表示认可，并进行了代码审查，确认了多个补丁的有效性和必要性。

总的来说，本周的讨论推动了补丁的进一步完善，确保了其在实际应用中的有效性和稳定性。

#### 📝 邮件列表

1. **[02-03 10:30]** [PATCH v2 00/14] KVM: arm64: Support FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-03 10:30]** [PATCH v2 01/14] drivers/perf: apple_m1: Refactor event select/filter configuration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-03 10:31]** [PATCH v2 03/14] drivers/perf: apple_m1: Provide helper for mapping PMUv3 events
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-03 10:31]** [PATCH v2 06/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-03 10:31]** [PATCH v2 07/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-03 10:31]** [PATCH v2 10/14] KVM: arm64: Move PMUVer filtering into KVM code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[02-19 16:22]** Re: [PATCH v2 01/14] drivers/perf: apple_m1: Refactor event select/filter configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-19 16:37]** Re: [PATCH v2 03/14] drivers/perf: apple_m1: Provide helper for mapping PMUv3 events
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-19 16:45]** Re: [PATCH v2 06/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-19 17:44]** Re: [PATCH v2 07/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-19 18:17]** Re: [PATCH v2 10/14] KVM: arm64: Move PMUVer filtering into KVM code
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[02-19 11:22]** Re: [PATCH v2 07/14] KVM: arm64: Use a cpucap to determine if system
 supports FEAT_PMUv3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[02-19 11:25]** Re: [PATCH v2 06/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[02-19 19:35]** Re: [PATCH v2 07/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-20 13:48]** [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[02-20 13:48]** [PATCH v2 01/14] arm64: cpufeature: Handle NV_frac as a synonym of NV2
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[02-20 13:48]** [PATCH v2 02/14] KVM: arm64: Hide ID_AA64MMFR2_EL1.NV from guest and userspace
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[02-20 13:48]** [PATCH v2 03/14] KVM: arm64: Mark HCR.EL2.E2H RES0 when ID_AA64MMFR1_EL1.VH is zero
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[02-20 13:48]** [PATCH v2 04/14] KVM: arm64: Mark HCR.EL2.{NV*,AT} RES0 when ID_AA64MMFR4_EL1.NV_frac is 0
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[02-20 13:48]** [PATCH v2 05/14] KVM: arm64: Advertise NV2 in the boot messages
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[02-20 13:48]** [PATCH v2 06/14] KVM: arm64: Consolidate idreg callbacks
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[02-20 13:49]** [PATCH v2 07/14] KVM: arm64: Make ID_REG_LIMIT_FIELD_ENUM() more widely available
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[02-20 13:49]** [PATCH v2 08/14] KVM: arm64: Enforce NV limits on a per-idregs basis
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[02-20 13:49]** [PATCH v2 09/14] KVM: arm64: Move NV-specific capping to idreg sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[02-20 13:49]** [PATCH v2 10/14] KVM: arm64: Allow userspace to limit NV support to nVHE
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[02-20 13:49]** [PATCH v2 11/14] KVM: arm64: Make ID_AA64MMFR4_EL1.NV_frac writable
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[02-20 13:49]** [PATCH v2 12/14] KVM: arm64: Advertise FEAT_ECV when possible
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[02-20 13:49]** [PATCH v2 13/14] KVM: arm64: Allow userspace to request KVM_ARM_VCPU_EL2*
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[02-20 13:49]** [PATCH v2 14/14] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[02-20 14:03]** Re: [PATCH v2 01/14] arm64: cpufeature: Handle NV_frac as a synonym
 of NV2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
31. **[02-20 14:04]** Re: [PATCH v2 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Joey Gouly <joey.gouly@arm.com>
32. **[02-20 21:13]** Re: [PATCH v2 06/14] KVM: arm64: Consolidate idreg callbacks
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
33. **[02-20 18:36]** Re: [PATCH v2 02/14] KVM: arm64: Hide ID_AA64MMFR2_EL1.NV from guest
 and userspace
   - 发件人: Sebastian Ott <sebott@redhat.com>
34. **[02-20 19:46]** Re: [PATCH v2 02/14] KVM: arm64: Hide ID_AA64MMFR2_EL1.NV from guest and userspace
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[02-21 08:52]** Re: [PATCH v2 02/14] KVM: arm64: Hide ID_AA64MMFR2_EL1.NV from guest
 and userspace
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 2: [PATCH 00/15] arm: rework id register storage

**📧 邮件数**: 15 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  7 Feb 2025 12:02:33 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM 架构的 ID 寄存器存储重构的补丁系列，共包含 15 个补丁。历史讨论中，Cornelia Huck 提出了这一补丁系列的背景，旨在为 CPU 模型的支持奠定基础，并提到补丁内容来自于更大的 CPU 模型系列。补丁的具体内容包括添加新的寄存器定义、存储主机特性到 ID 寄存器的访问器、以及生成 ID 寄存器定义的基础设施等。

在之前的讨论中，Richard Henderson 对某些补丁提出了意见，认为某些内容不应包含在当前补丁中，并建议在构建时生成文件而不是提交生成的文件。此外，讨论中还提到需要手动导入 Linux 的 sysreg 文件，以便分析潜在的破坏。

在本周的新讨论中，Eric Auger 对补丁内容进行了进一步的探讨，提出了对宏和查找过程的重构，并表示他有一个本地分支正在进行相关工作。此外，他建议将某些基础设施的内容推迟到主要的 CPU 模型系列中进行处理。这些讨论显示出参与者们对补丁的细节和未来工作的关注。

#### 📝 邮件列表

1. **[02-07 12:02]** [PATCH 00/15] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[02-07 12:02]** [PATCH 01/15] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[02-07 12:02]** [PATCH 02/15] arm/kvm: add accessors for storing host features into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[02-07 12:02]** [PATCH 03/15] arm/cpu: Store aa64isar0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[02-07 12:02]** [PATCH 13/15] arm/cpu: Add infra to handle generated ID register definitions
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[02-07 12:02]** [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[02-07 10:46]** Re: [PATCH 03/15] arm/cpu: Store aa64isar0 into the idregs arrays
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
8. **[02-07 11:02]** Re: [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
9. **[02-10 16:20]** Re: [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[02-18 16:22]** Re: [PATCH 01/15] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Eric Auger <eric.auger@redhat.com>
11. **[02-18 16:33]** Re: [PATCH 02/15] arm/kvm: add accessors for storing host features
 into idregs
   - 发件人: Eric Auger <eric.auger@redhat.com>
12. **[02-18 16:38]** Re: [PATCH 15/15] arm/cpu: Add generated files
   - 发件人: Eric Auger <eric.auger@redhat.com>
13. **[02-18 16:53]** Re: [PATCH 03/15] arm/cpu: Store aa64isar0 into the idregs arrays
   - 发件人: Eric Auger <eric.auger@redhat.com>
14. **[02-18 16:54]** Re: [PATCH 02/15] arm/kvm: add accessors for storing host features
 into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[02-18 17:06]** Re: [PATCH 13/15] arm/cpu: Add infra to handle generated ID register
 definitions
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 3: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 18 Feb 2025 14:39:55 -0600

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 ARM64 架构上启用分支栈采样的补丁（PATCH v20 00/11）。该补丁引入了一个名为分支记录缓冲扩展（BRBE）的新特性，旨在支持 ARM64 的性能监控。

**补丁内容**：
补丁系列的主要目标是实现对 ARM64 架构中 BRBE 的支持，允许在执行过程中记录分支信息。补丁分为多个部分，其中前七个补丁主要是清理和准备工作，后四个补丁则实现了 BRBE 的具体支持。

**历史讨论要点**：
在之前的讨论中，补丁经历了多次版本迭代，逐步完善了对异常类型的处理、事件和分支权限的要求等。补丁的 v19 版本中，开发者们对分支记录的保存和处理进行了重要修改，确保在任务调度时不会丢失记录。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的具体实现细节上，包括如何处理不同的异常类型、如何优化分支记录的清理和无效化过程等。此外，开发者们对补丁进行了测试，James Clark 提供了测试反馈，表明补丁在实际应用中表现良好。整体来看，补丁的开发进展顺利，预计将很快合并到主线代码中。

#### 📝 邮件列表

1. **[02-18 14:39]** [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[02-18 14:39]** [PATCH v20 01/11] perf: arm_pmuv3: Call kvm_vcpu_pmu_resync_el0()
 before enabling counters
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[02-18 14:39]** [PATCH v20 02/11] perf: arm_pmu: Don't disable counter in
 armpmu_add()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[02-18 14:39]** [PATCH v20 03/11] perf: arm_pmuv3: Don't disable counter in
 armv8pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
5. **[02-18 14:39]** [PATCH v20 04/11] perf: arm_v7_pmu: Drop obvious comments for
 enabling/disabling counters and interrupts
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
6. **[02-18 14:40]** [PATCH v20 05/11] perf: arm_v7_pmu: Don't disable counter in
 (armv7|krait_|scorpion_)pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
7. **[02-18 14:40]** [PATCH v20 06/11] perf: apple_m1: Don't disable counter in
 m1_pmu_enable_event()
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
8. **[02-18 14:40]** [PATCH v20 07/11] perf: arm_pmu: Move PMUv3-specific data
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
9. **[02-18 14:40]** [PATCH v20 08/11] arm64/sysreg: Add BRBE registers and fields
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
10. **[02-18 14:40]** [PATCH v20 09/11] arm64: Handle BRBE booting requirements
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
11. **[02-18 14:40]** [PATCH v20 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
12. **[02-18 14:40]** [PATCH v20 11/11] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
13. **[02-19 16:09]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 4: [PATCH 0/2] KVM: arm64: EL2 PMU reset handling fixes

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 17 Feb 2025 11:24:10 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 EL2 PMU（Performance Monitoring Unit）复位处理的修复补丁。该补丁主要包括两个部分：

1. **原始补丁内容**：补丁旨在修复在复位时 MDCR_EL2.HPMN 字段的默认值设置为 0 的问题，并确保 PMCR_EL0.P 的写入能够正确复位所有计数器，而不仅仅是“来宾”视图。

2. **之前讨论要点**：参与者 Marc Zyngier 和 Joey Gouly 讨论了 PMU 测试中遇到的行为不符合预期的问题，指出 MDCR_EL2.HPMN 应该在热复位时重置为 NUM_PMU_COUNTERS，而不是 0。此外，PMCR_EL0.P 的写入行为也需要进行调整，以确保在 EL2 中写入时能够清除所有计数器。

3. **本周新讨论与进展**：本周的讨论中，Marc Zyngier 提出了两个补丁的具体实现，分别是修复 MDCR_EL2.HPMN 的复位值和调整 PMCR_EL0.P 的处理逻辑。Oliver Upton 对这两个补丁进行了审核并表示支持。Joey Gouly 也确认这些补丁解决了他测试中的问题。此外，Vipin Sharma 提出了 KVM 自测试运行器的补丁，旨在增强测试的执行和管理功能。

总体来看，本周的讨论集中在补丁的具体实现和测试验证上，参与者们积极反馈并提出了进一步的改进建议。

#### 📝 邮件列表

1. **[02-17 11:24]** [PATCH 0/2] KVM: arm64: EL2 PMU reset handling fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-17 11:24]** [PATCH 1/2] KVM: arm64: Fix MDCR_EL2.HPMN reset value
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-17 11:24]** [PATCH 2/2] KVM: arm64: Contextualise the handling of PMCR_EL0.P writes
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-17 10:33]** Re: [PATCH 2/2] KVM: arm64: Contextualise the handling of PMCR_EL0.P
 writes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-17 10:53]** Re: [PATCH 1/2] KVM: arm64: Fix MDCR_EL2.HPMN reset value
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-19 14:03]** Re: [PATCH 1/2] KVM: arm64: Fix MDCR_EL2.HPMN reset value
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-19 11:04]** Re: [PATCH 1/2] KVM: arm64: Fix MDCR_EL2.HPMN reset value
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[02-19 21:10]** Re: [PATCH 1/2] KVM: arm64: Fix MDCR_EL2.HPMN reset value
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-20 10:44]** Re: [PATCH 0/2] KVM: arm64: EL2 PMU reset handling fixes
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[02-21 16:59]** [PATCH 0/2] Add KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
11. **[02-21 16:59]** [PATCH 1/2] KVM: selftests: Add default testfiles for KVM selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
12. **[02-21 16:59]** [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>

---

### Thread 5: [PATCH v2 0/4] KVM: arm64: writable MIDR/REVIDR

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 11 Feb 2025 15:39:06 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构中允许用户空间修改 MIDR（主 ID 寄存器）和 REVIDR（修订 ID 寄存器）的补丁系列。

1. **原始补丁内容**：Sebastian Ott 提出的补丁系列（PATCH v2 0/4）旨在使虚拟机监控器（VMM）能够修改 MIDR 和 REVIDR，以支持在不同机器之间迁移。该补丁的变化包括让来宾能够观察到修改后的 MIDR_EL1 值、增加了额外的 .set_user 函数以及自测试功能。

2. **之前讨论要点**：在历史讨论中，参与者对补丁的实现提出了多项技术性问题和建议，特别是关于 VPIDR_EL2 寄存器的处理和在不同 vCPU 上的 MIDR 值一致性问题。Marc Zyngier 和 Oliver Upton 等人对补丁的细节进行了深入探讨，提出了改进建议。

3. **本周新讨论及进展**：在本周的讨论中，Yonggang Luo 表示在应用 Oliver 的修改后，问题得到了解决，MIDR_EL1 的修改成功生效，并分享了测试结果。Sebastian Ott 也对 Oliver 的建议表示认可，并表示正在进行进一步的测试。这表明补丁系列的实施取得了积极进展，且参与者之间的协作有效推动了问题的解决。

#### 📝 邮件列表

1. **[02-11 15:39]** [PATCH v2 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-11 15:39]** [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-15 02:13]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[02-16 00:16]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: =?UTF-8?B?572X5YuH5YiaKFlvbmdnYW5nIEx1byk=?= <luoyonggang@gmail.com>
5. **[02-15 16:41]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-16 03:04]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: =?UTF-8?B?572X5YuH5YiaKFlvbmdnYW5nIEx1byk=?= <luoyonggang@gmail.com>
7. **[02-16 18:09]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-17 02:55]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: =?UTF-8?B?572X5YuH5YiaKFlvbmdnYW5nIEx1byk=?= <luoyonggang@gmail.com>
9. **[02-16 19:06]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-17 14:40]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: =?UTF-8?B?572X5YuH5YiaKFlvbmdnYW5nIEx1byk=?= <luoyonggang@gmail.com>
11. **[02-17 16:06]** Re: [PATCH v2 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 6: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 9 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 10:12:19 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM64 架构下内存管理的一个补丁系列，主要目的是去除 `PXD_TABLE_BIT` 的定义，以便在即将支持的 D128 页面表中实现更好的抽象。

**原始补丁/问题内容**：
补丁系列的核心是移除 `PXD_TABLE_BIT` 定义，转而依赖于更抽象的 `PXX_TYPE_MASK`、`PXX_TYPE_SECT` 和 `PXX_TYPE_TABLE`。这种改变旨在适应 D128 页面表的需求，因为 D128 模型中没有单一的页面表位来区分表与块，而是使用跳过级别（SKL）字段。

**之前讨论要点**：
在之前的讨论中，补丁的初版（V1）已提出了类似的修改，但未能完全解决与 D128 模型的兼容性问题。此次更新（V2）对 `pmd_mkhuge()` 和 `pud_mkhuge()` 的实现进行了修改，并增加了对 `pud_bad()` 的补丁，以确保在创建映射时正确处理类型掩码。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁系列的具体实现上，Anshuman Khandual 提出了多个补丁，逐步清理和替换原有的 `PXD_TABLE_BIT` 相关代码。具体包括在创建段映射时清除 `PXX_TYPE_MASK`、在检查页面表条目时使用新的类型掩码等。此外，Ryan Roberts 也参与了讨论，提出了对 `pud_bad()` 和 `pmd_trans_huge()` 的改进，确保在不同配置下的正确性。最终，所有 `PXD_TABLE_BIT` 宏都被删除，标志着这一系列补丁的完成。

#### 📝 邮件列表

1. **[02-21 10:12]** [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-21 10:12]** [PATCH V2 1/8] KVM: arm64: ptdump: Test PMD_TYPE_MASK for block mapping
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-21 10:12]** [PATCH V2 2/8] arm64/ptdump: Test PMD_TYPE_MASK for block mapping
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-21 10:12]** [PATCH V2 3/8] arm64/mm: Clear PXX_TYPE_MASK in mk_[pmd|pud]_sect_prot()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-21 10:12]** [PATCH V2 4/8] arm64/mm: Clear PXX_TYPE_MASK and set PXD_TYPE_SECT in [pmd|pud]_mkhuge()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[02-21 10:12]** [PATCH V2 5/8] arm64/mm: Check PXD_TYPE_TABLE in [p4d|pgd]_bad()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[02-21 10:12]** [PATCH V2 6/8] arm64/mm: Check PUD_TYPE_TABLE in pud_bad()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
8. **[02-21 10:12]** [PATCH V2 7/8] arm64/mm: Check pmd_table() in pmd_trans_huge()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
9. **[02-21 10:12]** [PATCH V2 8/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 7: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired

**📧 邮件数**: 9 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 07 Feb 2025 17:45:33 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在为模拟定时器设置 ISTATUS（中断状态），当定时器过期时生效。

**原始补丁/问题内容**：
补丁的目的是解决在虚拟机迁移过程中，由于对 ID 寄存器的支持不完整而导致的迁移失败问题。Marc Zyngier 提到，当前的实现可能会在恢复 ID 寄存器时出现问题。

**之前讨论要点**：
在历史讨论中，参与者们探讨了如何使用 vCPU 特性标志来更好地描述 NV（非易失性）特性，并讨论了 ID 寄存器的某些字段在虚拟机初始化后的状态如何影响用户空间的期望。Eric Auger 提到他已经更新了 nv-next 分支，以期改善迁移的稳定性。

**本周新讨论与进展**：
本周，Ganapatrao Kulkarni 报告了在使用 nv-next 分支时出现的内核崩溃问题，原因是 QEMU 在保存和恢复寄存器时试图写入未分配的 ID 寄存器。Ganapatrao 提出了修复方案，并计划对 ID_UNALLOCATED 进行重构，以确保其具有正确的名称和功能。Marc Zyngier 对此表示赞同，并确认在调试过程中，寄存器名称的缺失导致了额外的困难。最终，Ganapatrao 表示他已将代码重构并重新基于 nv-next，问题已得到解决。

#### 📝 邮件列表

1. **[02-07 17:45]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-07 10:09]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If
 timer expired
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[02-07 18:38]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-10 19:26]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer
 expired
   - 发件人: Eric Auger <eauger@redhat.com>
5. **[02-15 17:50]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-18 13:03]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer
 expired
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
7. **[02-18 16:33]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-18 21:24]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer expired
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-20 11:40]** Re: [PATCH] KVM: arm64: nv: Set ISTATUS for emulated timers, If timer
 expired
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 8: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 14:02:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 ARM64 平台的虚拟机实时迁移中的错误管理（Errata management）问题，主要涉及一系列补丁（patch）更新。

1. **原始补丁内容**：补丁集 [PATCH v8 0/6] 旨在改进 KVM 在 ARM64 平台上处理虚拟机迁移时的错误管理，特别是与 CPU 的 MIDR/REVIDR 值相关的错误处理。补丁通过引入新的超调用（hypercall）和寄存器来支持目标实现的检索，以便在迁移时处理不同平台的错误。

2. **之前讨论要点**：在历史讨论中，补丁经历了多个版本的迭代，主要集中在修复编译错误、引入新的寄存器 KVM_REG_ARM_VENDOR_HYP_BMAP_2 以支持新超调用、以及增加自测功能等。参与者对补丁的功能和实现细节进行了多次反馈和修改。

3. **本周的新讨论与进展**：本周的讨论中，Shameer Kolothum 提交了补丁 v8 的多个部分，主要包括：
   - 修复了编译错误并添加了 R-by 标签。
   - 引入了两个新的超调用，用于检索目标 CPU 实现的信息。
   - 增加了 KVM_REG_ARM_VENDOR_HYP_BMAP_2 寄存器，以支持新的超调用功能。
   - 将 _midr_in_range_list() 函数导出，以便后续补丁访问新数据。
   - 通过超调用启用与实现 CPU 相关的错误处理。
   - 增加了自测功能以验证新寄存器的行为。

整体来看，本周的讨论集中在补丁的实现细节和功能验证上，参与者积极提供反馈，推动补丁的完善和测试。

#### 📝 邮件列表

1. **[02-21 14:02]** [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-21 14:02]** [PATCH v8 1/6] arm64: Modify _midr_range() functions to read MIDR/REVIDR internally
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[02-21 14:02]** [PATCH v8 2/6] KVM: arm64: Introduce hypercall support for retrieving target implementations
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
4. **[02-21 14:02]** [PATCH v8 3/6] KVM: arm64: Introduce KVM_REG_ARM_VENDOR_HYP_BMAP_2
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
5. **[02-21 14:02]** [PATCH v8 4/6] =?UTF-8?q?arm64:=20Make=20=C2=A0=5Fmidr=5Fin=5Fran?= =?UTF-8?q?ge=5Flist()=20an=20exported=20function?=
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
6. **[02-21 14:02]** [PATCH v8 5/6] smccc/kvm_guest: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
7. **[02-21 14:02]** [PATCH v8 6/6] KVM: selftests: Add test for KVM_REG_ARM_VENDOR_HYP_BMAP_2
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>

---

### Thread 9: [PATCH 00/14] KVM: arm64: NV userspace ABI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 15 Feb 2025 17:38:02 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH 00/14] KVM: arm64: NV userspace ABI”，主要涉及对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的用户空间 ABI（应用程序二进制接口）的修订。

**原始 patch/问题内容**：
Marc Zyngier 提出了一个新的补丁系列，旨在修正之前 ABI 的问题，使其更符合 KVM 的当前操作方式。补丁中取消了对 NV 特定调整的需求，并通过 vcpu 标志完全选择 NV 配置。同时，保留了 KVM_ARM_VCPU_EL2 标志以启用 NV，并新增了 KVM_ARM_VCPU_EL2_E2H0 标志，以限制 NV 行为。

**之前讨论要点**：
在历史讨论中，Marc 提到补丁系列的功能几乎完整，并希望用户空间能够请求 KVM_ARM_VCPU_EL2*，因此需要提升 KVM_VCPU_MAX_FEATURES 的值。此外，补丁还包括对 NV caps 和 vcpu 标志的文档说明。

**本周的新讨论、进展或结论**：
本周的讨论中，Oliver Upton 对补丁表示认可，计划在 6.15 版本中合并前 12 个补丁。Oliver 还对补丁 13 和 14 进行了审核，并给予了“Reviewed-by”标记。此外，Marc 还提到修复了一个导致 ID_UNALLOCATED() 寄存器处理错误的bug，进一步简化了 ID_DESC() 宏的复杂性。整体来看，讨论进展顺利，补丁准备工作逐步推进。

#### 📝 邮件列表

1. **[02-15 17:38]** [PATCH 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-15 17:38]** [PATCH 13/14] KVM: arm64: Allow userspace to request KVM_ARM_VCPU_EL2*
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-15 17:38]** [PATCH 14/14] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-19 15:17]** Re: [PATCH 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[02-19 15:19]** Re: [PATCH 13/14] KVM: arm64: Allow userspace to request
 KVM_ARM_VCPU_EL2*
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[02-19 15:19]** Re: [PATCH 14/14] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[02-20 13:07]** Re: [PATCH 00/14] KVM: arm64: NV userspace ABI
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v19 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 02 Feb 2025 18:42:54 -0600

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构上启用分支栈采样的补丁（[PATCH v19 00/11]），该补丁利用了 v9.2 架构特性——分支记录缓冲扩展（BRBE）。补丁的主要目的是支持在 arm64 上进行性能监测的分支栈采样。

在历史讨论中，参与者 Rob Herring 提到该补丁系列经过多次重构，主要的改动集中在第 11 个补丁上。补丁 1-7 是一些独立的清理和准备工作，之前已经发布过。讨论中，Leo Yan 提出了关于在 nVHE（非虚拟化高特权模式）客户机中禁用分支生成的必要性，强调了在进入客户机之前需要保存和禁用 BRBE 状态，并在返回主机时恢复该状态。

在本周的新讨论中，Rob Herring 对于 BRBCR 寄存器的读取提出了看法，认为必须读取该寄存器以确认 BRBE 是否启用，因为 PAUSED 状态在复位后是未知的。他指出，无论是读取还是写入寄存器，开销是相同的。这一讨论进一步推动了对补丁的理解和完善。

#### 📝 邮件列表

1. **[02-02 18:42]** [PATCH v19 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[02-02 18:43]** [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[02-13 17:03]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Leo Yan <leo.yan@arm.com>
4. **[02-13 17:16]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring <robh@kernel.org>
5. **[02-14 09:55]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Leo Yan <leo.yan@arm.com>
6. **[02-18 08:17]** Re: [PATCH v19 10/11] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring <robh@kernel.org>

---

### Thread 11: [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Feb 2025 15:02:55 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM（paravirtualized KVM）初始化问题，主要集中在 HCRX_EL2 和其他陷阱的设置。

**原始 patch/问题的内容**：
Fuad Tabba 提出的补丁（PATCH v1 0/3）旨在修复 pKVM 中 HCRX_EL2 陷阱的初始化问题。当前 pKVM 的行为是在第一次运行主机 vcpu 时初始化 hyp 视图，但由于引入了 kvm_calculate_traps() 函数，一些主机陷阱值在对应 vcpu 首次运行时才会计算，导致 pKVM 获取到错误的视图。

**之前讨论要点**：
在历史讨论中，Fuad 提出了两个补丁，强调在主机 vcpu 首次运行时应逐个初始化 hyp vcpu，而不是一次性初始化所有 hyp vcpu，以确保能够获取到完整的主机状态。

**本周的新讨论、进展或结论**：
本周的讨论中，Will Deacon 对补丁表示认可，并提出了关于潜在 Spectre 攻击的担忧，建议在索引前进行安全检查。Fuad 也同意了这个建议，并表示将考虑在后续的补丁系列中解决 pKVM 中的类似安全访问问题。整体来看，讨论集中在如何确保 pKVM 的安全性和正确性上，且双方对补丁的方向达成了一致。

#### 📝 邮件列表

1. **[02-14 15:02]** [PATCH v1 0/3] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-14 15:02]** [PATCH v1 3/3] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-17 15:30]** Re: [PATCH v1 3/3] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-17 15:41]** Re: [PATCH v1 3/3] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[02-17 15:56]** Re: [PATCH v1 3/3] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-18 09:27]** Re: [PATCH v1 3/3] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 12: [PATCH V2 0/5] mm: Rework generic PTDUMP configs

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 17 Feb 2025 09:52:15 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是对 Linux 内核中的通用 PTDUMP 配置进行重构，涉及到五个补丁（PATCH V2 0/5）。该补丁系列的主要目的是在进行一些基本清理后，重命名通用 PTDUMP 配置，以提高可读性和明确性。

在历史讨论中，补丁的初步版本（V1）已经提出了对 GENERIC_PTDUMP 的依赖性进行调整，主要是为了避免在不支持该功能的平台上启用它，从而导致构建失败。补丁 V2 进一步删除了一些不必要的配置选项，并对文档进行了相应的更新。

本周的新讨论中，Anshuman Khandual 提出了五个具体补丁的详细内容：
1. 从 debug.config 中删除 GENERIC_PTDUMP 配置。
2. 从 mpc885_ads_defconfig 中删除 GENERIC_PTDUMP。
3. 从 arm64 的 ptdump 文档中删除 PTDUMP 配置选项。
4. 将 DEBUG_WX 的依赖关系更改为依赖于 GENERIC_PTDUMP。
5. 将 GENERIC_PTDUMP 和 PTDUMP_CORE 重命名为 ARCH_HAS_PTDUMP 和 PTDUMP，以消除混淆。

这些补丁已在 arm64 平台上进行了测试，并且在其他平台上也能成功构建。整体来看，本周的讨论集中在清理和重命名配置选项，以提高内核配置的清晰度和可维护性。

#### 📝 邮件列表

1. **[02-17 09:52]** [PATCH V2 0/5] mm: Rework generic PTDUMP configs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-17 09:52]** [PATCH V2 1/5] configs: Drop GENERIC_PTDUMP from debug.config
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-17 09:52]** [PATCH V2 2/5] arch/powerpc: Drop GENERIC_PTDUMP from mpc885_ads_defconfig
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[02-17 09:52]** [PATCH V2 3/5] docs: arm64: Drop PTDUMP config options from ptdump.rst
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[02-17 09:52]** [PATCH V2 4/5] mm: Make DEBUG_WX depdendent on GENERIC_PTDUMP
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[02-17 09:52]** [PATCH V2 5/5] mm: Rename GENERIC_PTDUMP and PTDUMP_CORE
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 13: [PATCH v4 00/27] KVM: arm64: Implement support for SME in
 non-protected guests

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Feb 2025 01:57:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于在非保护性虚拟机中实现对SME（Scalable Matrix Extension）支持的补丁（[PATCH v4 00/27] KVM: arm64: Implement support for SME in non-protected guests）。该补丁的主要内容是为KVM（Kernel-based Virtual Machine）在arm64架构上提供对SME的支持，重点关注用户空间ABI（应用二进制接口）的设计以及如何处理与PSTATE（处理器状态寄存器）相关的寄存器访问。

在历史讨论中，参与者Mark Brown和Marc Zyngier就补丁的设计细节进行了深入探讨，特别是关于如何在不破坏现有ABI的情况下实现SME支持，以及在处理异常和上下文切换时的复杂性。Marc Zyngier强调了保护模式的重要性，并指出需要在补丁中全面考虑KVM的各个方面。

本周的新讨论中，Marc Zyngier继续关注PSTATE的定义及其与SPSR（状态寄存器）的关系，提出了对架构文档中PSTATE布局的疑问，并讨论了在不启用SME的情况下，VMM（虚拟机监控程序）应如何保持现有行为。两位参与者就如何确保补丁符合架构预期进行了进一步的交流，Marc Zyngier明确表示，如果VMM不启用SME，则不应看到任何变化。

总体来看，讨论围绕补丁的实现细节、架构一致性及其对现有系统的影响展开，参与者们在寻求解决方案的同时，关注架构定义的准确性和补丁的可行性。

#### 📝 邮件列表

1. **[02-14 01:57]** [PATCH v4 00/27] KVM: arm64: Implement support for SME in
 non-protected guests
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[02-14 09:24]** Re: [PATCH v4 00/27] KVM: arm64: Implement support for SME in non-protected guests
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-14 15:13]** Re: [PATCH v4 00/27] KVM: arm64: Implement support for SME in
 non-protected guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[02-17 09:37]** Re: [PATCH v4 00/27] KVM: arm64: Implement support for SME in non-protected guests
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-18 22:54]** Re: [PATCH v4 00/27] KVM: arm64: Implement support for SME in
 non-protected guests
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 14: [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 18 Feb 2025 17:34:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM (Kernel-based Virtual Machine) 的补丁系列，主要涉及 arm64 架构下的可写 MIDR (Main ID Register)、REVIDR (Revision ID Register) 和 AIDR (Auxiliary ID Register)。

1. **原始补丁内容**：该补丁系列允许虚拟机监控器（VMM）修改 MIDR、REVIDR 和 AIDR，以支持在不同机器间迁移时的寄存器变更。这些寄存器主要用于处理硬件缺陷，因此与之前的缺陷管理系列补丁相关联。

2. **之前讨论要点**：在之前的讨论中，补丁的设计考虑了如何让来宾操作系统能够观察到这些寄存器的变化，并确保在虚拟 CPU 上下文中正确处理相关寄存器的状态。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括：
   - 允许用户空间写入 MIDR_EL1、REVIDR_EL1 和 AIDR_EL1，并确保这些更改对来宾可见。
   - 进行了自测，确保这些寄存器的写入操作能够成功，并在虚拟 CPU 重置后保持其值。
   - 讨论了补丁的代码变更，涉及多个文件的修改，确保寄存器的读写逻辑正确。

整体来看，这一补丁系列的实施将增强 KVM 在处理不同硬件平台间的迁移能力，提升虚拟化的灵活性和稳定性。

#### 📝 邮件列表

1. **[02-18 17:34]** [PATCH v3 0/4] KVM: arm64: writable MIDR/REVIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-18 17:34]** [PATCH v3 1/4] KVM: arm64: Allow userspace to change MIDR_EL1
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-18 17:34]** [PATCH v3 2/4] KVM: arm64: Allow userspace to change REVIDR_EL1
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[02-18 17:34]** [PATCH v3 3/4] KVM: arm64: Allow userspace to change AIDR_EL1
   - 发件人: Sebastian Ott <sebott@redhat.com>
5. **[02-18 17:34]** [PATCH v3 4/4] KVM: selftests: arm64: Test writes to MIDR,REVIDR,AIDR
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 15: [PATCH v7 0/5] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 14 Feb 2025 15:13:38 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上进行虚拟机实时迁移的错误管理的补丁（PATCH v7 0/5）。该补丁的主要内容是引入新的 KVM_REG_ARM_VENDOR_HYP_BMAP_2 寄存器，以支持新的超调用，并为该寄存器添加了自测功能。

在历史讨论中，参与者们对补丁进行了多次审查和建议。Shameer Kolothum 提出了补丁的更新，并提供了测试链接。Sebastian Ott 和 Marc Zyngier 也对补丁的实现提出了改进建议，例如导出某些功能以便于配置和优化代码结构。

在本周的新讨论中，Shameer 对 Sebastian 的建议表示感谢，并表示会考虑这些意见进行修改。这表明补丁仍在积极完善中，开发者们对改进的方向保持开放态度。整体来看，讨论集中在如何优化错误管理和增强补丁的功能性上。

#### 📝 邮件列表

1. **[02-14 15:13]** [PATCH v7 0/5] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[02-14 15:13]** [PATCH v7 4/5] smccc/kvm_guest: Enable errata based on implementation CPUs
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
3. **[02-14 17:12]** Re: [PATCH v7 4/5] smccc/kvm_guest: Enable errata based on implementation
 CPUs
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[02-14 16:43]** Re: [PATCH v7 4/5] smccc/kvm_guest: Enable errata based on implementation CPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-18 07:40]** RE: [PATCH v7 4/5] smccc/kvm_guest: Enable errata based on
 implementation CPUs
   - 发件人: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>

---

### Thread 16: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  3 Feb 2025 10:38:21 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的 EL2 要求，以支持 FEAT_PMUv3p9 特性。历史讨论中，Anshuman Khandual 提出了一个补丁系列（PATCH V2 0/7），旨在为 EL2 提供更精细的陷阱控制，以支持 PMU 相关寄存器（如 PMICNTR_EL0、PMICFILTR_EL0 和 PMUACR_EL1），以防止它们在 EL1 中的访问陷入 EL2。补丁中提到，PMZR_EL0 寄存器的陷阱控制暂时保持不变，因为该寄存器在内核中未被访问。

在本周的新讨论中，Anshuman Khandual 对补丁的状态进行了跟进，询问是否需要做出任何修改。Catalin Marinas 回复称已将该补丁应用到 arm64 的 for-next/el2-enable-feat-pmuv3p9 分支，并指出其他相关的系统寄存器补丁已应用到 arm64 for-next/sysreg 分支，以便在需要时可以被拉入其他树中（例如 KVM）。这表明补丁的进展顺利，相关工作正在进行中。

#### 📝 邮件列表

1. **[02-03 10:38]** [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-17 11:12]** Re: [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[02-18 19:03]** Re: (subset) [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[02-18 19:06]** Re: (subset) [PATCH V2 0/7] arm64/boot: Enable EL2 requirements for
 FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 17: [PATCH] arm64: kvm: ptdump: Initialize .owner fields of kvm_*_operations

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 23 Feb 2025 16:08:44 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的 KVM（Kernel-based Virtual Machine）补丁，主要目的是初始化 `kvm_*_operations` 结构中的 `.owner` 字段，以防止在这些操作仍在使用时卸载模块。

在本周的讨论中，Salah Triki 提出了一个补丁，具体内容是在 `kvm_ptdump_guest_fops`、`kvm_pgtable_range_fops` 和 `kvm_pgtable_levels_fops` 中添加 `.owner = THIS_MODULE` 的初始化。这一修改旨在确保在相关操作被使用时，模块不会被意外卸载，从而提高系统的稳定性。

Marc Zyngier 对此补丁表示好奇，询问具体是指哪个模块。这表明他对补丁的背景和影响有进一步的关注，可能希望了解更多上下文信息。

总体而言，本周的讨论围绕补丁的具体实现和潜在影响展开，Marc 的提问为后续讨论提供了进一步的思考方向。

#### 📝 邮件列表

1. **[02-23 16:08]** [PATCH] arm64: kvm: ptdump: Initialize .owner fields of kvm_*_operations
   - 发件人: Salah Triki <salah.triki@gmail.com>
2. **[02-23 18:21]** Re: [PATCH] arm64: kvm: ptdump: Initialize .owner fields of kvm_*_operations
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH] KVM: arm64: Ensure a VMID is allocated before programming VTTBR_EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 19 Feb 2025 14:07:37 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下确保在编程 VTTBR_EL2 之前分配 VMID（虚拟机标识符）的补丁。该补丁由 Oliver Upton 提出，目的是解决在将 VMID 附加到阶段 2 MMU 时可能出现的竞争条件，这种情况可能导致 vCPU 以 VMID 为 0 进入来宾系统。

在历史讨论中，Vladimir 报告了这个竞争条件的问题，指出在 KVM_RUN 循环中，VMID 的附加过程与 MMU 的加载过程并不同步，可能导致硬件在一段时间内错误地配置为 VMID 0，这显然是不合理的。因此，Oliver 建议在加载 VTTBR_EL2 之前，提前分配 VMID，以避免这种情况。

在本周的新讨论中，Oliver 提交的补丁得到了 Marc Zyngier 的认可，并已被应用到修复中。补丁的实现修改了相关的代码，确保在编程 VTTBR_EL2 之前，VMID 已被正确分配，从而提升了系统的稳定性和安全性。

#### 📝 邮件列表

1. **[02-19 14:07]** [PATCH] KVM: arm64: Ensure a VMID is allocated before programming VTTBR_EL2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[02-20 16:42]** Re: [PATCH] KVM: arm64: Ensure a VMID is allocated before programming VTTBR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH] KVM: arm64: Fix tcr_el2 initialisation in hVHE mode

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Feb 2025 13:37:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要针对 hVHE 模式下 TCR_EL2 的初始化问题。

在历史讨论中，Will Deacon 提出了一个补丁，指出在非 VHE 模式下，cpu_prepare_hyp_mode() 函数使用主机的 TCR_EL1 设置来计算 TCR_EL2 的值。然而，在 hVHE 模式下，TCR_EL2 的某些字段（如 T1SZ 和 IPS）出现了错误，导致初始化过程不正确。

在本周的新讨论中，Marc Zyngier 对该补丁进行了确认，并表示已经将其应用于修复中，补丁的提交哈希为 102c51c50db88aedd00a318b7708ad60dbec2e95。这表明该问题得到了及时解决，并且补丁已被纳入代码库。

总结来说，此次讨论围绕 KVM 在 hVHE 模式下的 TCR_EL2 初始化问题展开，经过讨论后，相关补丁已成功应用。

#### 📝 邮件列表

1. **[02-14 13:37]** [PATCH] KVM: arm64: Fix tcr_el2 initialisation in hVHE mode
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-19 22:11]** Re: [PATCH] KVM: arm64: Fix tcr_el2 initialisation in hVHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH v1] KVM: arm64: vgic-its: Add debugfs interface to expose ITS tables

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Feb 2025 18:02:58 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 架构中，为 VGIC 中的中断翻译服务（ITS）表添加 debugfs 接口的补丁（PATCH v1）。该补丁旨在通过 debugfs 接口展示 ITS 表的内容，以便于对中断路由配置进行检查和调试。

在历史讨论中，Jing Zhang 提出了该补丁，介绍了 ITS 表的功能，即将设备/事件 ID 映射到中断 ID 和目标处理器，并以表格形式展示相关数据。这一补丁的目的是简化调试过程，使开发者能够更方便地查看中断相关信息。

在本周的新讨论中，Marc Zyngier 对补丁提出了一些反馈。他质疑补丁中展示的输出是否合理，并建议将调试相关的代码集中在 vgic-debug.c 文件中，而不是分散在多个地方。此外，他指出补丁中只考虑了设备表，建议在注释中明确说明这一点。他还提到使用十六进制表示设备 ID 更为常见，并建议使用 kasprintf() 来提高代码的稳定性。

总体来看，本周的讨论集中在补丁的实现细节和代码结构的优化上，提出了多项改进建议。

#### 📝 邮件列表

1. **[02-13 18:02]** [PATCH v1] KVM: arm64: vgic-its: Add debugfs interface to expose ITS tables
   - 发件人: Jing Zhang <jingzhangos@google.com>
2. **[02-19 21:51]** Re: [PATCH v1] KVM: arm64: vgic-its: Add debugfs interface to expose ITS tables
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v2] KVM: arm64: vgic-its: Add debugfs interface to expose ITS tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 20 Feb 2025 14:42:46 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VGIC（Virtual Generic Interrupt Controller）中引入一个 debugfs 接口，以便展示 ITS（Interrupt Translation Service）表的内容。

**原始 patch/问题的内容**：
该 patch 提出了一个 debugfs 接口，用于显示 VGIC ITS 表的内容。这些表将设备/事件 ID 映射到中断 ID 和目标处理器。通过 debugfs 接口，用户可以更方便地检查和调试中断路由配置。

**之前讨论要点**：
历史讨论部分没有相关内容，因此没有提供背景讨论。

**本周的新讨论、进展或结论**：
本周的讨论中，Jing Zhang 提交了 patch v2，主要改进包括将代码从 vgic-its-debug.c 移动到 vgic-debug.c，并解决了之前版本中 Marc 提出的其他意见。该 patch 通过 seq_file 接口以表格形式展示 ITS 表数据，输出为只读，旨在用于调试和信息查看。该接口的实现允许高效处理可能较大的 ITS 表。整体来看，本周的进展主要集中在代码结构的调整和对前期反馈的响应。

#### 📝 邮件列表

1. **[02-20 14:42]** [PATCH v2] KVM: arm64: vgic-its: Add debugfs interface to expose ITS tables
   - 发件人: Jing Zhang <jingzhangos@google.com>

---

### Thread 22: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 19 Feb 2025 14:30:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构上为 Realms 启用内存加密的补丁（PATCH v7 09/11）。该补丁旨在确保在运行 Realm 客户端时，能够正确处理页面共享和保护。

在历史讨论中，虽然没有具体的历史邮件记录，但可以推测出该补丁的提出是为了改进当前的内存管理机制，以支持 Realm 客户端的功能。

本周的讨论中，参与者 Steven Price 提出了两个主要选项来解决当前存在的问题。首先，他指出当前对 `is_realm_world()` 的调用时机过早，可能导致某些 Realm 客户端无法与主机共享页面。为了解决这个问题，Steven 提出了两个选项：一是将 `rodata_full` 设为 Realm 客户端的必需项，二是重新考虑在早期检测 Realm 客户端的想法，以便解决早期控制台（earlycon）的问题。

Steven 目前倾向于第一个选项，因为它已经是默认设置，但他也意识到如果需要修复早期控制台或发现其他类似问题，第二个选项将更有意义。他还附上了未测试的补丁代码，并建议更新文档以反映这些更改。

#### 📝 邮件列表

1. **[02-19 14:30]** Re: [PATCH v7 09/11] arm64: Enable memory encrypt for Realms
   - 发件人: Steven Price <steven.price@arm.com>

---

## 📌 RFC

共 4 个 thread

---

### Thread 1: [RFC PATCH 0/2] Add NV Selftest cases

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Feb 2025 08:41:18 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM（Kernel-based Virtual Machine）中添加 NV（Nested Virtualization）自测用例的补丁系列。补丁的主要内容是修改 KVM 自测代码，以支持在 vEL2（作为客体虚拟机监控器）中运行客体代码，并添加测试用例以验证客体代码的启动和 VNCR 映射寄存器的访问。

在历史讨论中，参与者 Ganapatrao Kulkarni 提出了两个补丁，分别是添加客体虚拟机监控器测试和访问 VNCR 映射寄存器的自测用例。Marc Zyngier 提出了对补丁的反馈，建议在测试中显式设置 HCR_EL2 和 MDCR_EL2 寄存器的值，以确保客体行为的可靠性，并讨论了如何使现有测试能够在 EL2 客体中运行。

在本周的新讨论中，Ganapatrao Kulkarni 进一步澄清了关于 TPIDR_EL2 的写入问题，提出在测试代码中应始终写入 TPIDR_EL1，并在客体代码中将其值复制到 TPIDR_EL2，或在 vcpu 设置过程中同时写入两个寄存器。这一讨论为补丁的进一步完善提供了方向。

#### 📝 邮件列表

1. **[02-06 08:41]** [RFC PATCH 0/2] Add NV Selftest cases
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[02-06 08:41]** [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
3. **[02-06 21:14]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-07 18:56]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor
 test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
5. **[02-07 13:59]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor test
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-07 22:16]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor
 test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
7. **[02-19 18:17]** Re: [RFC PATCH 1/2] KVM: arm64: nv: selftests: Add guest hypervisor
 test
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 2: [RFC PATCH v3 1/3] KVM: arm64: SIGBUS VMM for SEA guest abort

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 23:29:57 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理同步外部中止（SEA）时的改进，主要通过发送 SIGBUS 信号来提高虚拟机监控器（VMM）和虚拟 CPU（vCPU）的错误处理能力。

**原始 Patch 内容**：
Jiaqi Yan 提出的补丁（RFC PATCH v3 1/3）旨在改进 KVM 对 SEA 的处理。当 APEI（高级平台错误接口）无法处理同步外部中止时，KVM 将通过发送 SIGBUS 信号来通知 VMM/vCPU，而不是直接导致虚拟机内核崩溃。此补丁的主要目的是使 KVM 的处理方式与核心内核一致，从而提高错误恢复的优雅性。

**之前讨论要点**：
在之前的讨论中，参与者关注了如何更好地处理内存错误，尤其是在 VMM 需要跟踪受损内存页的情况下。补丁的设计考虑了在处理内存错误时，如何减少对整个虚拟机的影响。

**本周新讨论与进展**：
本周的讨论中，Jiaqi Yan 提出了补丁的后续版本，包括对 vCPU ESR_ELx 中 FnV 位的设置，以便在处理 SEA 时提供更准确的信息。此外，补充了关于新用户空间 API 的文档，允许用户空间在处理不可纠正的内存错误时注入 SEA。Marc Zyngier 提出了对补丁的反馈，建议去掉 RFC 标记，并讨论了将信号处理转变为 VM 退出的可能性。他强调了在处理内存错误时，VMM 需要能够提供更多的可调试信息，而不是简单地依赖信号机制。Jiaqi Yan 表示将考虑这些反馈，并在下一个版本中进行改进。

#### 📝 邮件列表

1. **[02-20 23:29]** [RFC PATCH v3 1/3] KVM: arm64: SIGBUS VMM for SEA guest abort
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[02-20 23:29]** [RFC PATCH v3 2/3] KVM: arm64: set FnV in vcpu's ESR_ELx when host
 FAR_EL2 is invalid
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[02-20 23:29]** [RFC PATCH v3 3/3] Documentation: kvm: new UAPI when arm64 guest
 consumes UER
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[02-21 15:15]** Re: [RFC PATCH v3 1/3] KVM: arm64: SIGBUS VMM for SEA guest abort
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-21 22:22]** Re: [RFC PATCH v3 1/3] KVM: arm64: SIGBUS VMM for SEA guest abort
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 3: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 17:45:26 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM 单元测试的补丁（patch），其主要内容是将所有非 x86 的条件编译指令从 `__ASSEMBLY__` 更改为 `__ASSEMBLER__`，并移除所有手动定义的 `__ASSEMBLY__`。该补丁旨在解决在 x86 汇编文件中包含某些受 `__ASSEMBLY__` 保护的头文件时遇到的问题。

在历史讨论中，虽然没有具体的补丁或详细的讨论记录，但可以推测出该问题的背景是由于 `__ASSEMBLY__` 是从 Linux 内核中继承而来，且需要手动定义，导致在编译时出现问题。而 `__ASSEMBLER__` 则是由编译器自动定义的，使用更为方便。

在本周的新讨论中，补丁的作者 Sean Christopherson 提出了这一修改，并强调该补丁尚未经过测试，属于一种“愤怒补丁”，因为他在调试过程中耗费了大量时间。补丁涉及到 37 个文件的修改，主要是将条件编译指令进行替换。作者表示，x86 目前不依赖于 `__ASSEMBLY__`，并正在进行并行的清理工作。

总体来看，此次讨论集中在提升代码的可维护性和减少编译问题上，期待后续的测试结果和进一步的反馈。

#### 📝 邮件列表

1. **[02-21 17:45]** [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 4: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 18 Feb 2025 09:52:35 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 Arm 架构上实现 SMMUv3 驱动的补丁（RFC PATCH v2 00/58），主要针对 pKVM（用于增强虚拟化的内核模块）进行探讨。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在为 pKVM 提供对 Arm SMMUv3 的支持，以改善虚拟化性能和功能。参与者提到，pKVM 并不强调稳定的 ABI（应用二进制接口），这意味着在实现过程中可能会面临一些挑战。

本周的讨论中，Tian, Kevin 表达了对 pKVM 实现的看法。他指出，虽然 KVM-Arm 从一开始就已经适应了硬件限制，但在此基础上添加 pKVM 的概念相对简单。然而，为了支持这种分离模型，其他子系统的改动可能会增加维护负担，这可能会让维护者质疑支持 pKVM 的价值，特别是当维护成本过高时。Kevin 认为，未来的讨论将有助于评估这一补丁的可行性和价值。

#### 📝 邮件列表

1. **[02-18 09:52]** RE: [RFC PATCH v2 00/58] KVM: Arm SMMUv3 driver for pKVM
   - 发件人: Tian, Kevin <kevin.tian@intel.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #3

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 20 Feb 2025 17:44:06 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 Linux 6.14 版本中的修复，特别是针对 MMU（内存管理单元）相关的错误。

1. **原始 patch/问题的内容**：本次补丁主要解决了两个 MMU 相关的错误。第一个错误涉及 hVHE EL2 的 stage-1，错误地从错误的寄存器获取 ASID（地址空间标识符）。第二个错误则影响 VHE，导致其可能使用过时的 VMID（虚拟机标识符）值。

2. **之前的讨论要点**：由于本周邮件中没有提及历史讨论，因此无法提供相关的背景信息。

3. **本周的新讨论、进展或结论**：本周，Marc Zyngier 提交了针对上述问题的修复补丁，并请求 Paolo 进行合并。这些修复包括修正 TCR_EL2 配置，确保在编程 VTTBR_EL2 之前分配 VMID，从而避免因未分配 VMID 而导致的竞争条件。补丁涉及对四个文件的修改，增加了 22 行代码，删除了 30 行代码，旨在提高系统的稳定性和性能。

总的来说，本周的讨论集中在解决 KVM/arm64 的 MMU 错误上，确保系统在运行时的可靠性。

#### 📝 邮件列表

1. **[02-20 17:44]** [GIT PULL] KVM/arm64 fixes for 6.14, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 10 Feb 2025 10:41:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试的补丁，主题为“如果未配置为 QEMU，则拒绝运行测试”。该补丁旨在确保测试脚本在未正确配置的情况下不会执行，从而避免潜在的错误。

在历史讨论中，参与者主要关注如何改进脚本的结构。Alexandru Elisei 提出了创建一个新的脚本文件（如 vmm.bash），以便集中管理函数的调用，确保所有相关脚本可以共享必要的功能。Andrew Jones 则建议优先考虑现有的 arch-run.bash 或 common.bash 文件，而不是创建新文件。他们讨论了如何在脚本中添加条件检查，以确保目标支持性。

在本周的新讨论中，Al Dunsmuir 对之前的讨论进行了语法上的小修正，指出在某个条件下应该跳过自测设置，具体是“./arm/run 不支持 'kvmtool'”。这表明参与者在细节上仍在进行审查和完善，确保补丁的准确性和有效性。

总体来看，邮件讨论围绕如何优化测试脚本的结构和逻辑展开，确保在不支持的环境下能够安全地跳过测试。

#### 📝 邮件列表

1. **[02-10 10:41]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[02-10 14:56]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[02-10 18:04]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[02-17 11:02]** Re: [kvm-unit-tests PATCH v2 03/18] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Al Dunsmuir <al.dunsmuir@sympatico.ca>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/7] arm64: support EL2

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 14:13:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 单元测试的补丁系列，旨在支持在 EL2（异常级别2）下运行这些测试。该补丁系列包含七个补丁，主要涉及对现有代码的修改和新功能的添加。

在历史讨论中，补丁的背景是为了扩展对嵌套虚拟化的测试支持，并确保这些测试也能在裸金属环境下正常工作。Joey Gouly 提到了一些测试的现状，包括 EFI/ACPI 变更尚未测试、PMU 测试存在问题等，并表示将继续调试。

本周的新讨论中，Joey 提出了七个具体补丁的详细内容，包括：
1. **补丁1**：如果启动时处于 EL2，则降级到 EL1。
2. **补丁2**：在 EL2 下使用虚拟化超时器。
3. **补丁3**：修复 EL2 下的计时器 IRQ。
4. **补丁4**：在 EL2 下使用 SMC（安全监控调用）而非 HVC（高虚拟化调用）。
5. **补丁5**：更新自测以支持在 EL2 下运行。
6. **补丁6**：在 EL2 下计数周期。
7. **补丁7**：如果支持 VHE（虚拟化硬件扩展），则在 EL2 下继续启动。

此外，Marc Zyngier 对某些代码提出了建议，建议使用符号常量表示 EL1t，并优化了代码中的某些逻辑。整体来看，补丁系列的目标是增强 KVM 单元测试在 ARM64 架构下的功能和稳定性。

#### 📝 邮件列表

1. **[02-20 14:13]** [kvm-unit-tests PATCH v1 0/7] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[02-20 14:13]** [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[02-20 14:13]** [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[02-20 14:13]** [kvm-unit-tests PATCH v1 3/7] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[02-20 14:13]** [kvm-unit-tests PATCH v1 4/7] arm64: micro-bench: use smc when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[02-20 14:13]** [kvm-unit-tests PATCH v1 5/7] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[02-20 14:13]** [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[02-20 14:13]** [kvm-unit-tests PATCH v1 7/7] arm64: run at EL2 if supported
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[02-20 15:23]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-20 15:34]** Re: [kvm-unit-tests PATCH v1 7/7] arm64: run at EL2 if supported
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 17:27:54 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 RISC-V 架构下的 KVM 单元测试中，允许使用其他 QEMU 模型的补丁。邮件的发起者是 Andrew Jones，主要提出了两个补丁。

第一个补丁（PATCH 1/2）旨在修改配置文件，以便支持所有架构的早期控制台（earlycon）功能。之前的讨论主要集中在如何将早期控制台的支持从特定于 ARM 的实现扩展到 RISC-V，确保在命令行中能够覆盖 UART 地址。

第二个补丁（PATCH 2/2）则引入了一个新的选项 `MACHINE_OVERRIDE`，允许 RISC-V 测试使用除默认的 'virt' 之外的其他 QEMU 机器类型。这一改动使得测试更加灵活，适应不同的硬件模型。

在本周的讨论中，Andrew Jones 提交了这两个补丁，并详细描述了每个补丁的目的和实现细节。补丁已完成初步开发，接下来可能会进行代码审查和测试，以确保其在不同 QEMU 模型下的兼容性和稳定性。整体来看，本周的进展表明了对 RISC-V 测试环境的持续改进和扩展。

#### 📝 邮件列表

1. **[02-21 17:27]** [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[02-21 17:27]** [kvm-unit-tests PATCH 1/2] configure: Allow earlycon for all architectures
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[02-21 17:27]** [kvm-unit-tests PATCH 2/2] riscv: Introduce MACHINE_OVERRIDE
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

